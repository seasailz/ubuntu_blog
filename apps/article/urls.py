# _*_ coding: utf-8 _*_
__date__ = '2019/9/17 22:58'

from django.urls import path
from article.views import ArticleDetailView, ArchivesView


app_name = '[article]'
urlpatterns = [
    path('detail/<int:article_id>', ArticleDetailView.as_view(), name='detail'),
    # 归档
    path('', ArchivesView.as_view(), name='arch_all'),
]
