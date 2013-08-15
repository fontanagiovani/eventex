# coding: utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('eventex.core.views',
                       url(r'^$', 'homepage', name='homepage'),
                       url(r'^palestrantes/(?P<slug>[\w-]+)/$','speaker_detail', name='speaker_detail'),
                       url(r'^palestras/$', 'talk_list', name='talk_list'),
                       )
