# _*_ coding: utf-8 _*_
__date__ = '2019/9/17 22:58'

from django.urls import path, re_path
from article.views import ArticleDetailView
from haystack.views import SearchView


app_name = '[article]'
urlpatterns = [
    path('detail/<int:article_id>', ArticleDetailView.as_view(), name='detail'),
    # re_path(r'search/$', SearchView(), name='haystack_search'),
]
