from django.http.response import HttpResponseBadRequest
from imfp.core.http_helpers import HttpJsonResponse
from imfp.events.forms import CreateEventForm, SubscribeToEventForm, UnsubscribeFromEventForm
from imfp.events.models import Event
from imfp.subscriptions.models import Subscription


def create_event(request):
    if request.method == 'POST':
        form = CreateEventForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # TODO figure out how i auth the user
            event = Event.objects.create_event(
                data['user_id'],
                data['description'],
                data['creation_time'],
                data['type'],
                data['address'],
                data['location'],
                data['zone'],
                data['type'],
                data['seats']
            )
            event.save()
            return HttpJsonResponse({'success': True})
        else:
            return HttpJsonResponse({'success': False, 'error': 'Invalid form data'})
    else:
        return HttpResponseBadRequest()


def subscribe_to_event(request, event_id):
    if request.method == 'POST':
        form = SubscribeToEventForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_id = data['user_id']
            subscription = Subscription.objects.create_subscription(user_id, event_id)
            if subscription:
                return HttpJsonResponse({'success': True})
            else:
                return HttpJsonResponse({'success': False, 'error': 'Subscribing to the event failed.'})
        else:
            return HttpJsonResponse({'success': False, 'error': 'Invalid form data'})
    else:
        return HttpResponseBadRequest()


def unsubscribe_from_event(request, event_id):
    if request.method == 'POST':
        form = UnsubscribeFromEventForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_id = data['user_id']
            success = Subscription.objects.remove_subscription(user_id, event_id)
            if success:
                return HttpJsonResponse({'success': True})
            else:
                return HttpJsonResponse({'success': False, 'error': 'Unsubscribing from event failed.'})
        else:
            return HttpJsonResponse({'success': False, 'error': 'Invalid form data'})
    else:
        return HttpResponseBadRequest()
