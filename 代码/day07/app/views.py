from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.artform import AddArtForm
from app.models import Article


def add_art(request):
    if request.method == 'GET':
        return render(request, 'add_article.html')

    if request.method == 'POST':
        # 吧提交的数据丢给表单AddArtForm做验证
        form = AddArtForm(request.POST, request.FILES)
        # is_valid()验证参数是否有效，如果参数验证成功，返回True，否则False
        if form.is_valid():
            # 表示字段验证成功
            title = form.data['title']
            desc = form.data['desc']
            content = form.data['content']
            icon = form.cleaned_data['icon']
            Article.objects.create(title=title, desc=desc, content=content, icon=icon)
            # return HttpResponseRedirect('/app/art')
            return HttpResponseRedirect(reverse('aap:art_list'))

        else:
            # 表示字段验证失败，需要将错误信息返回给页面展示
            return render(request, 'add_article.html', {'form': form})


def art(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        # page = request.GET.get('page') if request.GET.get('page') else 1
        # 第一种：使用切片完成分页
        # articles = Article.objects.all()[(page-1)*2: page*2]
        articles = Article.objects.all()
        # 将所有数据按照每一页3条数据军星切块处理
        paginator = Paginator(articles, 3)
        # 获取分页中的第几页数据
        page = paginator.page(page)
        return render(request, 'art.html', {'page': page})