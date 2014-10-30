from django.test.testcases import TestCase
from mock import Mock, patch
from imfp.events.views import list_events


class EventListViewTestCase(TestCase):

    def setUp(self):
        self.mock_user = Mock()
        self.mock_user.is_authenticated = Mock()
        self.mock_user.is_authenticated.return_value = True

        self.mock_request = Mock()
        self.mock_request.method = 'GET'
        self.mock_request.user = self.mock_user

        self.mock_event = Mock(id=1)

    def test_invalid_request_method(self):
        self.mock_request.method = 'POST'
        result = list_events(self.mock_request)
        self.assertEquals(result.status_code, 400)

    def test_logged_out_user(self):
        self.mock_user.is_authenticated.return_value = False
        result = list_events(self.mock_request)
        self.assertEquals(result.status_code, 302)

    def test_successful_page_render(self):
        with patch('imfp.events.views.Event.objects.get_events_by_user') as mock_get_events_by_user:
            with patch('imfp.events.views.render') as mock_render:
                mock_get_events_by_user.return_value = [self.mock_event]
                list_events(self.mock_request)
        assert mock_render.called
