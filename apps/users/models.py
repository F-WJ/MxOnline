# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=7, choices=(("male", u"男"), ("female", "女")), default="female")
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name=u"验证码类型", choices=(("register", u"注册"), ("forget", u"找回密码")), max_length=10)
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

# 模板的名称
#     verbose_name
#     是该对象的一个可读性更好的唯一名字:
#     verbose_name = "pizza"
#     若未提供该选项, Django 则会用一个类名字的 munged 版本来代替: CamelCase becomes camel case.
#     verbose_name_plural
#     对象名字的复数:
#     verbose_name_plural = "stories"
#     若未提供该选项, Django会使用verbose_name + "s".
    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    # 一個Python“魔法”，返回任何對象的unicode“表示”。 這是Python和Django將在模型實例需要強制並顯示為純字符串時使用的。
    # 最值得注意的是，當您在交互式控制台或管理員中顯示對象時，會發生這種情況。 你總是想定義這個方法;
    # 默認是不是很有幫助。
    # https://docs.djangoproject.com/en/1.9/topics/db/models/
    def __unicode__(self):
        return '{0}{1}'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

