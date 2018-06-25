#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from shortly_app.views import red


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('shortly_app.urls')),
    url(r'^(?P<url_id>[0-9a-zA-Z\-]+)$', red),
    url(r'^api-auth/', include('rest_framework.urls'))
]
