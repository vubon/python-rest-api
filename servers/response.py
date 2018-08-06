"""
This is a basic response data
"""

import json


class Response:

    def __init__(self, status, data):
        self.status_code = status
        self.data = data

    def data_pass_with_status(self):
        serializer = json.dumps(self.data)

        return serializer, self.status_code
