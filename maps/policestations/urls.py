from django.conf.urls import patterns, url

from policestations import views

urlpatterns = patterns('',
    url(r'^$', views.map, name='map')
    )
