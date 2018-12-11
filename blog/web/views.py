from django.shortcuts import render

from back.models import Article


def index(request):
    if request.method == "GET":
        arts = Article.objects.all()
        return render(request, 'web/index.html', {'arts': arts})
