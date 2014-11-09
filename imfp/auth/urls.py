from django.conf.urls import patterns

import views

urlpatterns = patterns('', (r'^login/$', views.login))
