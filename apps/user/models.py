from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male', verbose_name='性别')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    work_experience = models.CharField(default='', max_length=1024, verbose_name='工作经历')
    edu_experience = models.CharField(default='', max_length=1024, verbose_name='学历')
    skill = models.CharField(default='', max_length=1024, verbose_name='技能')
    image = models.ImageField(upload_to='user/%Y/%m', max_length=100, null=True, blank=True, verbose_name='头像')

    class Meta:
        verbose_name = '个人简介'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    # 获取文章总数
    def get_article_num(self):
        return self.article_set.all().count()
