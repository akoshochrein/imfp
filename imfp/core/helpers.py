
import json

from django.http import HttpResponse


class HttpJsonResponse(HttpResponse):

    def __init__(self, data_dict):
        super(HttpJsonResponse, self).__init__(json.dumps(data_dict), content_type='application/json')
