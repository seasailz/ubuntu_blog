# _*_ coding: utf-8 _*_
__date__ = '2019/9/17 20:06'

from django.urls import path

from user.views import UserInfo, LoginView


app_name = '[user]'
urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('info', UserInfo.as_view(), name='info'),
]
