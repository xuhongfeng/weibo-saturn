#!/usr/bin/env python

import json

class User(object):
    
    KEY_NAME = "screen_name"
    KEY_UID = "id"
        
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

    def __str__(self):
        return "{uid:%d name:%s}" %(self.uid, self.name)

    @staticmethod
    def decodeFromDict(dictValue): 
        uid = dictValue[User.KEY_UID]
        name = dictValue[User.KEY_NAME]
        if isinstance(name, unicode):
            name = name.encode("UTF-8")
        return User(uid, name)

    @staticmethod
    def decodeFromJson(jsonValue):
        dictValue = json.loads(jsonValue)
        return User.decodeFromDict(dictValue)

    @staticmethod
    def decodeList(strJson):
        tDict = json.loads(strJson)
        tList = tDict["users"]
        userList = []
        for v in tList:
            u = User.decodeFromDict(v)
            userList.append(u)
        return userList
