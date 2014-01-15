from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'myproject.apps.notes.views.index_redirect', name='index_redirect'),
    url(r'^notes/', include('myproject.apps.notes.urls', namespace='notes', app_name='notes')),

    url(r'^admin/', include(admin.site.urls)),
)

