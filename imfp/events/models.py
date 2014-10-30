from django.contrib.auth.models import User
from django.db import models
from imfp.events.constants import EVENT_TYPES, EVENT_ZONES


class EventManager(models.Manager):

    def create_event(self, creator_user_id, description, creation_time, time, location, zone, type, seats):
        event = self.create(
            creator=User.objects.get(creator_user_id),
            description=description,
            creation_time=creation_time,
            time=time,
            location=location,
            zone=zone,
            type=type,
            seats=seats
        )
        return event

    def delete_event(self, requester_id, event_id):
        event = Event.objects.get(event_id)
        requester = User.objects.get(requester_id)

        if event.creator == requester:
            event.delete()
            return True
        else:
            return False

    def get_events_by_user(self, user):
        return Event.objects.filter(creator=user)


class Event(models.Model):
    creator = models.ForeignKey('User')
    description = models.CharField(max_length=255)
    creation_time = models.DateTimeField()
    time = models.DateTimeField()
    # todo figure out geodata with django_google_maps fields here
    address = models.TextField(max_length=200)
    type = models.CharField(max_length=32, choices=EVENT_TYPES)
    zone = models.CharField(max_length=32, choices=EVENT_ZONES)
    seats = models.IntegerField()

    objects = EventManager()
