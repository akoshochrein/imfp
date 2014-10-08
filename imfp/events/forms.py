from django import forms
from imfp.events.constants import EVENT_TYPES, EVENT_ZONES


class CreateEventForm(forms.Form):
    name = forms.CharField(max_length=255)
    seats = forms.IntegerField()
    time = forms.DateTimeField()
    type = forms.ChoiceField(choices=EVENT_TYPES)
    zone = forms.ChoiceField(choices=EVENT_ZONES)
