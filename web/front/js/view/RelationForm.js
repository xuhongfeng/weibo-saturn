/*jslint browser: true, devel: true, indent: 4, nomen:true, vars: true */
/*global define */

define(function (require, exports, module) {
    "use strict";

    var Backbone = require('../lib/backbone');

    var Form = Backbone.View.extend({
        el: 'form#form-relation',

        events: {
            'click .btn-submit': 'onSubmit'
        },

        initialize: function () {
            var form = this;
            this.$('.nick-name').keyup(function (e) {
                if (e.which === 13) {
                    form.onSubmit();
                }
            });
        },

        onSubmit: function (evt) {
            evt.preventDefault();
            var name = this.$('.nick-name').val();
            if (!name) {
                alert('请输入昵称');
            } else {
                window.location = 'weibo/relation?name=' + name;
            }
        }
    });

    return Form;
});
