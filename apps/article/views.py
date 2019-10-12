import time

from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q

from article.models import Article, Tag
from user.models import UserProfile
# Create your views here.


# 获取归档列表
def get_archives_list(all_article):
    # 归档
    first_article = Article.objects.all().order_by('-add_time').first()
    # 取最早的一条数据作为对比数据
    year, month = first_article.add_time.year, first_article.add_time.month
    archives_list = []
    count = 0
    for article in all_article:
        # 如果下一篇和上一篇的年份和月份相等，把当前月的文章数count+1
        if article.add_time.year == year and article.add_time.month == month:
            count += 1
        else:
            # 如果不相等，说明在新的一个月里写了新的文章
            # 先把当前月份的年月和文章数记录下来
            archives_list.append([year, month, count])
            # 再把新的月份赋值，当做对比数据
            year = article.add_time.year
            month = article.add_time.month
            # 这里之所以不是0，是因为已经循环过新文章，下一次循环就是新新文章了
            count = 1
    # 因为最后一篇文章不会在经过else里的append语句，无论最后相不相等，都要保存
    archives_list.append([year, month, count])
    # print(archives_list)  # [[2019, 9, 7], [2019, 8, 1]]
    return archives_list


class IndexView(View):
    def get(self, request):
        all_article = Article.objects.all().order_by('-add_time')
        user = UserProfile.objects.all().first()
        # 关键词搜索
        key_words = request.GET.get('keywords', '')
        if key_words:
            # __contains 作用类似以mysql的 like语句
            # 加多一个 i 的作用是不区分大小写
            all_article = all_article.filter(Q(title__icontains=key_words) |
                                             Q(content__icontains=key_words) |
                                             Q(introduce__icontains=key_words))
        # 获取分页
        page = request.GET.get('page', 1)
        page = int(page)
        paginator = Paginator(all_article, 4, 2)
        page_article = paginator.page(page)
        # 最热文章推荐
        new_article = Article.objects.all().order_by('-click_num')[:4]
        # 获取归档列表
        archives_list = get_archives_list(all_article)
        # 导航栏active
        cur_page = 'index'
        # 获取标签数
        tags = Tag.objects.all()
        return render(request, 'index.html', {
            'user': user,
            'page_art': page_article,
            'new_article': new_article,
            'archives_list': archives_list,
            'cur_page': cur_page,
            'tag_num': len(tags)
        })


# 文章详情页
class ArticleDetailView(View):
    def get(self, request, article_id):
        all_article = Article.objects.all().order_by('-add_time')
        curr_article = None
        for index, article in enumerate(all_article):
            if index == 0:
                previous_index = 0
                next_index = index + 1
            elif index == len(all_article) - 1:
                previous_index = index - 1
                next_index = index
            else:
                previous_index = index - 1
                next_index = index + 1
            if article.id == article_id:
                curr_article = article
                previous_article = all_article[previous_index]
                next_article = all_article[next_index]
                break
        curr_article.click_num += 1
        curr_article.save()
        return render(request, 'article_detail.html', {
            'article': curr_article,
            'previous_article': previous_article,
            'next_article': next_article
        })


# 归档总页
class ArchivesView(View):
    def get(self, request):
        all_article = Article.objects.all().order_by('-add_time')
        archives_list = get_archives_list(all_article)
        # 导航栏active
        cur_page = 'archives'
        return render(request, 'archives.html', {
            'archives_list': archives_list,
            'all_article': all_article,
            'cur_page': cur_page
        })


class ClassifyVIew(View):
    def get(self, request):
        user = UserProfile.objects.all().first()
        tags = Tag.objects.all()
        all_article = Article.objects.all().order_by('-add_time')
        # 筛选分类
        classify = request.GET.get('classify', '')
        if classify:
            all_article = all_article.filter(type=classify)
        # 筛选标签
        tag = request.GET.get('tag', '')
        if tag:
            all_article = all_article.filter(tag__tag=tag)
        # 获取分页
        page = request.GET.get('page', 1)
        page = int(page)
        paginator = Paginator(all_article, 4, 2)
        page_article = paginator.page(page)
        # 导航栏active
        cur_page = 'classify'
        return render(request, 'classify.html', {
            'user': user,
            'tags': tags,
            'page_art': page_article,
            'cur_page': cur_page,
            'classify': classify,
            'mark': tag
        })
