# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = '2017-05-01 22:40'

import xadmin

from .models import EmailVerifyRecord


# object为python最顶层的类,不能继承admin类
class EmailVerifyRecordAdmin(object):
    pass

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
