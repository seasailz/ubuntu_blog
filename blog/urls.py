"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include, re_path
import xadmin
from django.views.static import serve

from blog.settings import MEDIA_ROOT, STATIC_ROOT
from article.views import IndexView, ArchivesView, ClassifyVIew
from user.views import page_not_found, pag_error

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # 首页
    path('', IndexView.as_view(), name='index'),
    path('user/', include('user.urls', namespace='user')),
    path('article/', include('article.urls', namespace='article')),
    # 归档
    path('archives', ArchivesView.as_view(), name='archives'),
    # 分类
    path('classify', ClassifyVIew.as_view(), name='classify'),

    # ueditor
    path('ueditor/', include('DjangoUeditor.urls')),

    # 验证码
    re_path(r'^captcha/', include('captcha.urls')),

    # 搜索引擎
    re_path(r'^search/', include('haystack.urls')),

    # 配置media路径，使网页的图片能从后台输出显示出来
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}, name='media'),
    # setting中设置 debug=False后，配置路径使静态文件能加载
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}, name='static'),
]

# 404页面配置
handler404 = page_not_found
# 全局500页面配置
handler500 = pag_error
