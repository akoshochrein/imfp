from django.conf.urls import patterns

import api
import views

urlpatterns = patterns('event',
                       (r'^create/$', api.create_event,),
                       (r'^subscribe/(?P<event_id>\d+)$', api.subscribe_to_event,),
                       (r'^unsubscribe/(?P<event_id>\d+)$', api.unsubscribe_from_event,),
                       (r'^delete/(?P<event_id>\d+)$', api.delete_event,),
                       (r'^list/$', views.list_events,))
