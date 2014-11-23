from django.conf import settings
from django.conf.urls import patterns, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('', (r'^admin/', include(admin.site.urls)),)

if 'events' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', (r'^events/', 'events.urls'))

# if this is false, we are in a bad shape
'''
if 'core' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', (r'^', 'core.urls'))
'''
