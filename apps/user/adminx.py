# _*_ coding: utf-8 _*_
__date__ = '2019/9/18 13:43'

import xadmin
from xadmin import views


# 后台页面全局配置--主题功能
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


# 后台页面全局配置--页头页脚
class GlobalSetting(object):
    site_title = '个人博客'
    site_footer = '该网站由海涵制作'
    # 将导航栏以手风琴的样式收叠
    menu_style = 'accordion'


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
