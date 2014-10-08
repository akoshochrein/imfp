import datetime
from mock import Mock, patch
from django.test.testcases import TestCase
from imfp.events.api import create_event

__all__ = ['CreateEventTestCase']


class CreateEventTestCase(TestCase):

    def setUp(self):
        self.mock_request = Mock()
        self.mock_request.method = 'POST'
        self.mock_request.POST = {
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
