"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import blog.views as bv


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', bv.firstpage, name='firstpage'),
    url(r'^blog/$', bv.index, name='index'),
    url(r'^message/$', bv.message, name='message'),
    url(r'^ueditor/', include('DjangoUeditor.urls' )),
    url(r'^column/$', bv.column_page, name='column_page'),
    url(r'^articles/$', bv.article_page, name='article_page'),
    url(r'^column/(?P<column_slug>[^/]+)/$', bv.column_detail, name='column'),
    url(r'^blog/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$', bv.article_detail, name='article'),
]

from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)