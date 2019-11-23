from django.views import View
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q

import json

from user.models import UserProfile
from user.forms import LoginForm
# Create your views here.


# 重载方法 验证数据库账号密码
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Q用以 或
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # check_password 是AbstractUser的方法
            # 数据库中的密码是密文，而前端穿明文，用get直接查明文不行
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form': login_form})

    def post(self, request):
        # 表单验证
        login_form = LoginForm(request.POST)
        # 验证login_form中的_errors是否为空，为空则说明没有错误
        if login_form.is_valid():
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            # authenticate验证数据库是否正确，成功返回一个对象，否则返回none
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                # 直接render 会导致下次重新登录后主页没有数据
                # return render(request, 'index.html')
                # 页面重定向
                from django.urls import reverse
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html', {'msg': '账号或密码不正确', 'login_form': login_form})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class UserInfo(View):
    def get(self, request):
        user = UserProfile.objects.all().first()
        return render(request, 'user_info.html', {
            'user': user
        })


def page_not_found(request, exception):
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def pag_error(request):
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response
