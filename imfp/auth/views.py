from django.core.context_processors import csrf
from django.shortcuts import render_to_response


def login(request):
    return render_to_response('login.html', csrf(request))
