# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-10 06:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0003_auto_20181207_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='atype',
        ),
        migrations.DeleteModel(
            name='Atype',
        ),
    ]
