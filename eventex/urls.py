# coding utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'', include('eventex.core.urls', namespace='core')),
                       )


urlpatterns += patterns('django.views.static',
                        url(r'^static/(?P<path>.*)$', 'serve',
                            {'document_root': settings.STATIC_ROOT}),
                        )
