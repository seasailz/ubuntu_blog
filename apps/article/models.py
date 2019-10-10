from datetime import datetime

from django.db import models

from user.models import UserProfile
from DjangoUeditor.models import UEditorField
# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='作者')
    title = models.CharField(max_length=100, verbose_name='标题')
    introduce = models.CharField(max_length=100, null=True, blank=True, verbose_name='简介')
    # content = models.CharField(max_length=200, verbose_name='内容')
    content = UEditorField(verbose_name='内容', width=700, height=300, imagePath="article/ueditor/img/%(basename)s_%(date)s.%(extname)s",
                           filePath="article/ueditor/file/", upload_settings={"imageMaxSize": 1204000}, default='')
    type = models.CharField(max_length=2, choices=(('ht', '后台'), ('qd', '前端'), ('qt', '其他')), verbose_name='文章类型')
    image = models.ImageField(upload_to='article/%Y/%m', max_length=100, null=True, blank=True, verbose_name='封面图')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    click_num = models.IntegerField(default=0, verbose_name='点击数')

    class Meta:
        verbose_name = '文章'
        # 不加plural会使后台页面的导航名带一个字母's'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
