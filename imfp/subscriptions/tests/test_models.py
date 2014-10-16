
from django.test.testcases import TestCase
from mock import patch, Mock
from imfp.subscriptions.models import Subscription

__all__ = ['CreateSubscriptionTestCase', 'RemoveSubscriptionTestCase']


class SubscriptionOperationsTestBase(TestCase):

    def setUp(self):
        self.mock_event = Mock(id=1)
        self.mock_user = Mock(id=1)
        self.mock_subscription = Mock(user=self.mock_user, event=self.mock_event)
        self.subscription_manager = Subscription.objects


class CreateSubscriptionTestCase(SubscriptionOperationsTestBase):

    def test_get_event_returns_none(self):
        with patch('imfp.subscriptions.models.get_or_none') as mock_get_or_none:
            mock_get_or_none.return_value = None
            result = self.subscription_manager.create_subscription(self.mock_user.id, self.mock_event.id)
        self.assertEquals(result, None)

    # TODO figure this out.
    #def test_create_subscription_success(self):
    #    with patch('imfp.subscriptions.models.get_or_none'):
    #        with patch('imfp.subscriptions.models.create') as mock_create:
    #            with patch('imfp.subscriptions.models.save'):
    #                mock_create.return_value = self.mock_subscription
    #                result = self.subscription_manager.create_subscription(self.mock_user.id, self.mock_event.id)
    #    self.assertNotEquals(result, None)


class RemoveSubscriptionTestCase(SubscriptionOperationsTestBase):

    def test_get_event_returns_none(self):
        with patch('imfp.subscriptions.models.get_or_none') as mock_get_or_none:
            mock_get_or_none.return_value = None
            result = self.subscription_manager.remove_subscription(self.mock_user.id, self.mock_event.id)
        self.assertEquals(result, False)
