
from django.test.testcases import TestCase
from mock import patch, Mock
from imfp.events.models import Event

__all__ = ['DeleteEventTestCase']


class DeleteEventTestCase(TestCase):

    def setUp(self):
        self.mock_user = Mock(id=1)
        self.mock_other_user = Mock(id=1)
        self.mock_event = Mock(id=1, creator=self.mock_user)

    def test_requester_is_not_creator(self):
        with patch('imfp.events.models.Event.objects.get') as mock_get_event:
            with patch('imfp.events.models.User.objects.get') as mock_get_user:
                mock_get_event.return_value = self.mock_event
                mock_get_user.return_value = self.mock_other_user
                result = Event.objects.delete_event(self.mock_other_user.id, self.mock_event.id)
        self.assertEquals(result, False)

    def test_delete_successful(self):
        with patch('imfp.events.models.Event.objects.get') as mock_get_event:
            with patch('imfp.events.models.User.objects.get') as mock_get_user:
                mock_get_event.return_value = self.mock_event
                mock_get_user.return_value = self.mock_user
                result = Event.objects.delete_event(self.mock_user.id, self.mock_event.id)
        self.assertEquals(result, True)
