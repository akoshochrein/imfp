from imfp.subscriptions.models import Subscription


def user_is_subbed_to_event(user, event):
    return len(Subscription.objects.filter(user=user, event=event)) > 0
