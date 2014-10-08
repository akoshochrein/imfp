from django.http.response import HttpResponseBadRequest


def create_event(request):
    if request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()
