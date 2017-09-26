# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = '2017/8/16 21:14'
from django import forms
from captcha.fields import CaptchaField


# 登陆验证
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    # 可以减轻数据库负担
    password = forms.CharField(required=True, min_length=5)


# 注册验证
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})