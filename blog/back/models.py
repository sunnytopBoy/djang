from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)
    content = models.TextField()
    icon = models.ImageField(upload_to='article', null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'article'


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)

    class Meta:
        db_table = 'user'
