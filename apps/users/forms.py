# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = '2017/8/16 21:14'
from django import forms


# 验证
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    # 可以减轻数据库负担
    password = forms.CharField(required=True, min_length=5)
