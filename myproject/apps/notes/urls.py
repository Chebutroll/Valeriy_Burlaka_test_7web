from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
                       # url(r'^$', views.NotesList.as_view(), name='index_page')
                       url(r'^$', views.index_temp, name='index_page'),
                       )
