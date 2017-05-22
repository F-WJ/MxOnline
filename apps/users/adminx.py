# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = '2017-05-01 22:40'

import xadmin
from .models import EmailVerifyRecord, Banner


# object为python最顶层的类,不能继承admin类
class EmailVerifyRecordAdmin(object):
    # 设置显示内容
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索和导出
    search_fields = ['code', 'email', 'send_type']
    # 过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_dislay = ['title', 'image', 'url', 'index', 'add_time']
    search_fieds = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
