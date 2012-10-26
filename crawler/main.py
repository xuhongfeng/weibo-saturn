#!/usr/bin/env python

from store import Queue, UserStore, FriendsStore
from weibo import WeiboClient, ApiException
from data import User
import time
import const
import string

queue = Queue()
userStore = UserStore()
friendsStore = FriendsStore()
client = WeiboClient()

def main():
    initUid = const.initUid
    access_token = const.accessToken

    if queue.count()==0:
        queue.enqueue(initUid)

    while True:
        print 'step1: dequeue'
        uid = queue.dequeue()
        if uid is None:
            break
        try:
            print 'step2: dump friends'
            friends = client.dumpFriends(uid, access_token)
        except ApiException, e:
            print e
            if e.status == 403:
                print "reload config"
                const.loadConfig()
                access_token = const.accessToken
            queue.putFront(uid)
            time.sleep(60)
            continue
        except:
            print 'exception'
            queue.putFront(uid)
            time.sleep(60)
            continue
        friendIds = User.extractIds(friends)
        print 'step3: save friend ids'
        friendsStore.saveFriends(uid, friendIds)
        print 'step4: save every friend in user store'
        userStore.saveUsers(friends)
        print 'step5: get enqueue list'
        counts = friendsStore.counts(friendIds)
        enqueueList = []
        for i in range(len(friendIds)):
            if counts[i] != 0:
                enqueueList.append(friendIds[i])
        print 'step6: enqueue'
        queue.enqueuePipe(enqueueList)

        print 'friends.keyCount=%d' % friendsStore.keyCount()
        print '\n\n--------------------------------\n\n'

if __name__ == '__main__':
    main()
