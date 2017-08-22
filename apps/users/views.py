# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm


# 自定义后台认证
# 官方文档：https://docs.djangoproject.com/en/1.9/topics/auth/customizing/
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 使用类
class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            # django自带认证
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                # render官方文档网址https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/
                return render(request, "index.html")
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})

        else:
            return render(request, "login.html", {"login_form": login_form})


# request官方文档：https://docs.djangoproject.com/en/1.9/ref/request-response/
# # 自制登陆
# def user_login(request):
#     if request.method == "POST":
#         user_name = request.POST.get("username", "")
#         pass_word = request.POST.get("password", "")
#         # django自带认证
#         user = authenticate(username=user_name, password=pass_word)
#         if user is not None:
#             login(request, user)
#             # render官方文档网址https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/
#             return render(request, "index.html")
#         else:
#             return render(request, "login.html", {"msg":"用户名或密码错误！"})
#     elif request.method == "GET":
#         return render(request, "login.html", {})
