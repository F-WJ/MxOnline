# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm
from .forms import RegisterForm
from django.contrib.auth.hashers import make_password
from .models import UserProfile, EmailVerifyRecord
from utils.email_send import send_register_email


# 自定义后台认证
# 官方文档：https://docs.djangoproject.com/en/1.9/topics/auth/customizing/
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 验证码认证
class ActiveUserView(View):
    def get(self, request, active_code):
        # 从数据库查找验证码
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        return render(request, "login.html")



# 用户注册
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")
            # 导入数据库
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            # 用户状态为未激活
            user_profile.is_active = False
            # 加密
            user_profile.password = make_password(pass_word)
            # 保存
            user_profile.save()
            # 邮箱发送验证码
            send_register_email(user_name, "register")
            return render(request, "login.html")
        else:
            return render(request, "register.html")


# 使用类
# 登陆
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
                if user.is_active:
                    login(request, user)
                    # render官方文档网址https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {"msg": "用户未激活！"})
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
