# _*_ coding: utf-8 _*_
__date__ = '2019/9/20 16:58'
# 导入模板
from django import template

# 获取模板库对象
register = template.Library()


def to_str(month):
    str_month = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二']
    return str_month[month-1]


register.filter('to_str', to_str)
