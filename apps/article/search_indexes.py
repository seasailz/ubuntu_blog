# _*_ coding: utf-8 _*_
__date__ = '2019/11/27 9:14'

import datetime
from haystack import indexes
from article.models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
