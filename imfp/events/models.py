from django.contrib.auth.models import User
from django.db import models
from django_google_maps import fields as map_fields
from imfp.events.constants import EVENT_TYPES, EVENT_ZONES


class EventManager(models.Manager):

    def create_event(self, creator_user_id, description, creation_time, time, address, location, zone, type, seats):
        event = self.create(
            creator=User.objects.get(creator_user_id),
            description=description,
            creation_time=creation_time,
            time=time,
            address=address,
            location=location,
            zone=zone,
            type=type,
            seats=seats
        )
        return event


class Event(models.Model):
    creator = models.ForeignKey('User')
    description = models.CharField(max_length=255)
    creation_time = models.DateTimeField()
    time = models.DateTimeField()
    # todo figure out base fields here
    address = map_fields.AddressField(max_length=200)
    location = map_fields.GeoLocationField(max_length=100)
    type = models.CharField(max_length=32, choices=EVENT_TYPES)
    zone = models.CharField(max_length=32, choices=EVENT_ZONES)
    seats = models.IntegerField()

    objects = EventManager()
