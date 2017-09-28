# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from test_app.api_urls import api_v1


urlpatterns = [
    url(r'^api/v1/', include(api_v1.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url('', include('social_django.urls', namespace='social')),
    url(r'^', include('test_app.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
