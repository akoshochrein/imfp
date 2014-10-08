
from django.contrib.auth.models import User
from django.db import models
from django_google_maps import fields as map_fields
from constants import EVENT_TYPES, EVENT_ZONES


class Event(models.Model):
    creator = models.ForeignKey('UserProfile')
    creation_time = models.DateTimeField()
    event_time = models.DateTimeField()
    # todo figure out base fields here
    event_address = map_fields.AddressField(max_length=200)
    event_location = map_fields.GeoLocationField(max_length=100)
    event_type = models.CharField(max_length=32, choices=EVENT_TYPES)
    event_zone = models.CharField(max_length=32, choices=EVENT_ZONES)
    seats = models.IntegerField()


class Subscription(models.Model):
    event = models.ForeignKey(Event)
    user = models.OneToOneField(User)
