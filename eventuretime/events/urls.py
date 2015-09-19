from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^event/$', views.event, name='event'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^eventpage/$', views.eventpage, name='eventpage')

]