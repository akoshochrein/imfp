from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from imfp.events.constants import TEMPLATE_LIST
from imfp.events.models import Event


def list_events(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            user = request.user
            events = Event.objects.get_events_by_user(user)
            context = {
                'events': events
            }
            return render(request, TEMPLATE_LIST, context)
        else:
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseBadRequest()
