from django.contrib.auth.models import User
from django.db import models

from imfp.core.model_helpers import get_or_none
from imfp.events.models import Event


class SubscriptionManager(models.Manager):

    def create_subscription(self, user_id, event_id):

        event = get_or_none(Event, event_id)
        user = get_or_none(User, user_id)

        if event and user:
            if event.current_seats == 0:
                # TODO this Nonesense has to be fixed
                return None
            else:
                subscription = self.create(event=event, user=user)
                event.current_seats -= 1

                event.save()
                subscription.save()
                return subscription
        else:
            # TODO log
            pass

        return None

    def remove_subscription(self, user_id, event_id):

        event = get_or_none(Event, event_id)
        user = get_or_none(User, user_id)

        if event and user:
            try:
                subscription = self.filter(user=user, event=event)[0]

                # no tricks in my neighborhood
                event.current_seats = max(event.current_seats + 1, event.max_seats)
                event.save()

                subscription.delete()
                return True
            except IndexError:
                # TODO log
                return False
        else:
            # TODO log
            pass

        return False


class Subscription(models.Model):
    event = models.ForeignKey(Event)
    user = models.OneToOneField(User)

    objects = SubscriptionManager()
