from django.conf.urls import url

from . import views
#app

app_name = 'web'

urlpatterns = [

    url(r'^$', views.index_video, name='index_video'),
    url(r'^inicio$', views.inicio, name='inicio'),
    url(r'^obras/$', views.obras, name='obras'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^escuela/$', views.escuela, name='escuela'),
    url(r'^compania/$', views.compania, name='compania'),
    url(r'^yo_tambien/$', views.yotambien, name='yotambien'),
    url(r'^coloquios/$', views.coloquios, name='coloquios'),
    url(r'^malentendido/$', views.malentendido, name='malentendido'),
    url(r'^silencio/$', views.silencio, name='silencio'),
    url(r'^lagaviota/$', views.lagaviota, name='lagaviota'),
    url(r'^direcciones/$', views.direcciones, name='direcciones'),
    url(r'^brujas/$', views.brujas, name='brujas'),
    url(r'^bellcross/$', views.bellcross, name='bellcross')


]
