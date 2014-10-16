
from django.test.testcases import TestCase
from mock import patch
from imfp.core.model_helpers import get_or_none
from imfp.events.models import Event

__all__ = ['ModelHelpersTestCase']


# TODO this test case is incredibly pointless. I need to find a way to test these oneliners.
class ModelHelpersTestCase(TestCase):

    def setUp(self):
        self.mock_event_id = 1

    def test_get_or_none_returns_none(self):
        with patch('imfp.core.model_helpers.get_or_none') as mock_get_or_none:
            mock_get_or_none.return_value = None
            result = mock_get_or_none(Event, self.mock_event_id)
        self.assertEquals(result, None)
