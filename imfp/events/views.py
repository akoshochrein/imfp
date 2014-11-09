from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from imfp.events.constants import TEMPLATE_LIST
from imfp.events.models import Event
from imfp.subscriptions.herlpers import user_is_subbed_to_event


def list_events(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            user = request.user
            events = Event.objects.get_events_by_user(user)
            context = {
                'events': create_return_dict(user, events)
            }
            return render(request, TEMPLATE_LIST, context)
        else:
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseBadRequest()


# TODO this needs testing still
def create_return_dict(user, events):
    events_dictified = []
    for event in events:
        event_dictified = {
            'title': event.title,
            'creator': event.creator.user.username,
            'description': event.description,
            'time': event.time,
            'address': event.address,
            'user_is_going': user_is_subbed_to_event(user, event)
        }
        events_dictified.append(event_dictified)

    return events_dictified

