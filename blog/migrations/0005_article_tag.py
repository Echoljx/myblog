# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-07 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_article_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(default='', max_length=256, verbose_name='标签'),
        ),
    ]
