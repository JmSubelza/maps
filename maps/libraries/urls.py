from django.conf.urls import patterns, url

from libraries import views

urlpatterns = patterns('',
    url(r'^$', views.map, name='map')
    )
