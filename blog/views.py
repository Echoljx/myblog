
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Column, Article
from django.shortcuts import redirect


def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
    get_recent_article = Article.objects.all().order_by('pub_date')[:5]

    return render(request, 'index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
        'get_recent_article':get_recent_article,
    })

def firstpage(request):
    return HttpResponse(' ∑(っ °Д °;)っ没东西了！ 主页留着以后用(｡・`ω´･)')

def message(request):
    return render(request, 'message.html')


def column_page(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)

    return render(request, 'column_page.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
    })

def article_page(request):
    articles = Article.objects.all()
    return render(request, 'article_page.html', {'articles': articles})


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'blog/column.html', {'column': column})


def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)

    if article_slug != article.slug:
        return redirect(article, permanent=True)

    return render(request, 'blog/article.html', {'article': article})