# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from DjangoUeditor.models import UEditorField

from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('专栏名称', max_length=256)
    slug = models.CharField('专栏网址', max_length=256, db_index=True)
    intro = models.TextField('专栏简介', default='')

    column_img = models.ImageField(upload_to='column_img',default='pic_folder/None/no_image.pig')

    nav_display = models.BooleanField('导航显示', default=False)
    home_display = models.BooleanField('首页显示', default=False)

    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '专栏'
        verbose_name_plural = '专栏'
        ordering = ['name']  # 按照哪个专栏排序


@python_2_unicode_compatible
class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属专栏')

    tag = models.CharField('标签', max_length=256,default=u'')

    title = models.CharField('标题', max_length=256)

    article_img = models.ImageField(upload_to='article_img', default='pic_folder/None/no_image.pig')

    slug = models.CharField('网址', max_length=256, db_index=True)

    def get_absolute_url(self):
        return reverse('article', args=(self.pk, self.slug))

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    content = UEditorField('内容', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')

    published = models.BooleanField('正式发布', default=True)

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'