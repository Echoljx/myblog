# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-02 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171027_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='column_img',
            field=models.ImageField(default='pic_folder/None/no_image.pig', upload_to='column_img'),
        ),
    ]
