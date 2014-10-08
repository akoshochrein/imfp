
from django.contrib.auth.models import User
from django.db import models

from imfp.events.models import Event

class Subscription(models.Model):
    event = models.ForeignKey(Event)
    user = models.OneToOneField(User)
