from django.http.response import HttpResponseBadRequest
from imfp.core.helpers import HttpJsonResponse
from imfp.events.forms import CreateEventForm
from imfp.events.models import Event


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
