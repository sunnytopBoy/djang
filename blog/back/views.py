from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from back.ArticleForm import AddArtForm
from back.form import UserForm
from back.models import User, Article


def register(request):
    """
    注册
    :param request:用户名，密码，确认密码
    :return: 登录页面
    """
    if request.method == 'GET':
        return render(request, 'back/register.html')

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            pwd = form.data['pwd']
            pwd2 = form.data['pwd2']
            user = User.objects.filter(username=username).first()
            if user:
                err_name = '用户已经注册'
                return render(request, 'back/register.html', {'err_name': err_name, 'form': form})
            if pwd != pwd2:
                err_pwd = '两次密码不一致'
                return render(request, 'back/register.html', {'err_pwd': err_pwd, 'form': form})
            User.objects.create(username=username, password=pwd)

            return HttpResponseRedirect(reverse('back:login'))
        else:
            return render(request, 'back/register.html', {'form': form})


def login(request):
    """
    登录
    :param request:用户名，登录密码
    :return:首页
    """
    if request.method == 'GET':
        return render(request, 'back/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = User.objects.filter(username=username, password=pwd).first()
        if not user:
            err_user = '用户或密码不正确'
            return render(request, 'back/login.html', {'err_user': err_user})
        request.session['user_id'] = user.id
        return HttpResponseRedirect(reverse('back:index'))


def index(request):
    """
    首页
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'back/index.html')


def add_art(request):
    if request.method == 'GET':
        return render(request, 'back/add-article.html')
    if request.method == 'POST':
        # title = request.POST.get('title')
        # if not title:
        #     err_tit = '标题必填'
        #     return render(request, 'back/add-article.html', {'err_tit': err_tit})
        # Article.objects.create(title=title)
        form = AddArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            Article.objects.create(title=title, desc=desc, content=content, icon=icon)
            return HttpResponseRedirect(reverse('back:article'))
        return render(request, 'back/article.html', {'form': form})


def article(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        art = Article.objects.all()
        paginator = Paginator(art, 2)
        page = paginator.page(page)
        return render(request, 'back/article.html', {'page': page})



