import datetime
from mock import Mock, patch
from django.test.testcases import TestCase
from imfp.events.api import create_event, subscribe_to_event, unsubscribe_from_event

__all__ = ['CreateEventTestCase', 'SubscribeToEventTestCase']


class CreateEventTestCase(TestCase):

    def setUp(self):
        self.mock_request = Mock()
        self.mock_request.method = 'POST'
        self.mock_request.POST = {
            'user_id': 1,
            'name': 'Test Event',
            'description': 'test',
            'seats': 2,
            'time': datetime.datetime.strptime("22-DEC-2009", "%d-%b-%Y"),
            'type': 0,
            'zone': 0
        }

        self.mock_create_event = patch('imfp.events.api.Event.objects.create')

    def test_bad_request(self):
        self.mock_request.method = 'GET'
        response = create_event(self.mock_request)
        self.assertEquals(response.status_code, 400)

    def test_invalid_form(self):
        self.mock_request.POST.update({'type': -1})
        response = create_event(self.mock_request)
        self.assertEquals(response.content, '{"success": false, "error": "Invalid form data"}')

    def test_create_event_called(self):
        response = create_event(self.mock_request)
        self.assertEquals(response.content, '{"success": false, "error": "Invalid form data"}')


class EventActionTestBase(TestCase):

    def setUp(self):
        self.mock_event = Mock(id=1)
        self.mock_user = Mock(id=1)
        self.mock_subscription = Mock(event=self.mock_event, user=self.mock_user)

        self.mock_request = Mock()
        self.mock_request.method = 'POST'
        self.mock_request.POST = {'user_id': self.mock_user.id}


class SubscribeToEventTestCase(EventActionTestBase):

    def setUp(self):
        super(SubscribeToEventTestCase, self).setUp()

    def test_bad_request(self):
        self.mock_request.method = 'GET'
        response = subscribe_to_event(self.mock_request, self.mock_event.id)
        self.assertEquals(response.status_code, 400)

    def test_invalid_form(self):
        self.mock_user.id = 'lol'
        self.mock_request.POST = {'user_id': self.mock_user.id}
        response = subscribe_to_event(self.mock_request, self.mock_event.id)
        self.assertEquals(response.content, '{"success": false, "error": "Invalid form data"}')

    def test_failed_create_subscription(self):
        with patch('imfp.events.api.Subscription.objects.create_subscription') as mock_create_subscription:
            mock_create_subscription.return_value = None
            response = subscribe_to_event(self.mock_request, self.mock_event.id)
        self.assertEquals(response.content, '{"success": false, "error": "Subscribing to the event failed."}')

    def test_subscribe_success(self):
        with patch('imfp.events.api.Subscription.objects.create_subscription') as mock_create_subscription:
            mock_create_subscription.return_value = self.mock_subscription
            response = subscribe_to_event(self.mock_request, self.mock_event.id)
        self.assertEquals(response.content, '{"success": true}')


class UnsubscribeFromEventTestCase(EventActionTestBase):

    def setUp(self):
        super(UnsubscribeFromEventTestCase, self).setUp()

    def test_bad_request(self):
        self.mock_request.method = 'GET'
        response = unsubscribe_from_event(self.mock_request, self.mock_event.id)
        self.assertEquals(response.status_code, 400)

    def test_invalid_form(self):
        self.mock_user.id = 'lol'
        self.mock_request.POST = {'user_id': self.mock_user.id}
        response = unsubscribe_from_event(self.mock_request, self.mock_event.id)
        self.assertEquals(response.content, '{"success": false, "error": "Invalid form data"}')

    def test_failed_unsubscribe(self):
        with patch('imfp.events.api.Subscription.objects.remove_subscription') as mock_remove_subscription:
            mock_remove_subscription.return_value = False
            response = unsubscribe_from_event(self.mock_request, self.mock_event.id)
        self.assertEquals(response.content, '{"success": false, "error": "Unsubscribing from event failed."}')

    def test_successful_unsubscribe(self):
        with patch('imfp.events.api.Subscription.objects.remove_subscription') as mock_remove_subscription:
            mock_remove_subscription.return_value = True
            response = unsubscribe_from_event(self.mock_request, self.mock_event.id)
        self.assertEquals(response.content, '{"success": true}')
