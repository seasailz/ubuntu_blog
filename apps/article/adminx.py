# _*_ coding: utf-8 _*_
__date__ = '2019/9/18 10:30'

import xadmin
from article.models import Article, Tag, ArticleTag


class ArticleTagInLine(object):
    model = ArticleTag


class ArticleAdmin(object):
    # 导航栏的icon
    model_icon = 'fa fa-file-text-o'
    # 后台列表页显示的字段
    list_display = ['title', 'author', 'type', 'click_num', 'add_time']
    # 搜索关键词(注意:当字段是外键时，需要指明需要搜索的外键字段
    search_fields = ['title', 'author__username', 'type', 'content']
    # 筛选按钮筛选的字段
    list_filter = ['author', 'type', 'click_num', 'add_time', 'add_time']
    # 排序(进入后台默认排序
    ordering = ['-add_time']
    # 指明content字段采用富文本样式
    style_fields = {'content': 'ueditor'}
    inlines = [ArticleTagInLine]


class TagAdmin(object):
    model_icon = 'fa fa-file-text-o'
    list_display = ['tag', 'article']


class ArticleTagAdmin(object):
    model_icon = 'fa fa-file-text-o'
    list_display = ['article', 'tag']


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(ArticleTag, ArticleTagAdmin)
