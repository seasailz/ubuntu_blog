# _*_ coding: utf-8 _*_
__date__ = '2019/10/26 10:22'
"""
forms 表单预处理，减少数据库的查询负担
"""
from django import forms


# 预处理登录验证
class LoginForm(forms.Form):
    # 变量名必须和login.html中的name一致, required=true当字段为空报错
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)
