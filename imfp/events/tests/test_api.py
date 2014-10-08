from mock import Mock
from django.test.testcases import TestCase
from imfp.events.api import create_event

__all__ = ['CreateEventTestCase']


class CreateEventTestCase(TestCase):

    def setUp(self):
        self.mock_request = Mock()
        self.mock_request.method = 'POST'

    def test_bad_request(self):
        self.mock_request.method = 'GET'
        response = create_event(self.mock_request)
        self.assertEquals(response.status_code, 500)
