from django.conf.urls import patterns, url

from firestations import views

urlpatterns = patterns('',
    url(r'^$', views.map, name='map')
    )
