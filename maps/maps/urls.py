from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from maps import views

urlpatterns = patterns('',
     url(r'^libraries/', include('libraries.urls')),
     url(r'^police/', include('policestations.urls')),
     url(r'^fire/', include('firestations.urls')),
     url(r'^all/', views.map, name='map'),
     url(r'^$', direct_to_template, { 'template': 'home.html' }),
)
