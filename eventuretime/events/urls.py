from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^$', views.index, name='base'),
    url(r'^event/$', views.event, name='event'),
    url(r'^login/$', views.login, name='login'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^eventpage/(?P<event_id>\d+)$', views.eventpage, name='eventpage'),
    url(r'^events/new/$', views.new_event, name='new_event'),
    url(r'^events/mine/$', views.my_events, name='my_events'),
    url(r'^events/(?P<category>.+)/$', views.events_category, name='events_category'),
]