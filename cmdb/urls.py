# -*- coding: UTF-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = patterns('blog.views',
                       url()