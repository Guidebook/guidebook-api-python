import unittest

import mock

from guidebook import exceptions
from guidebook.api_requestor import APIRequestor


class TestAPIRequestor(unittest.TestCase):
    """
    Tests for APIRequestor
    """

    def test_status_code_to_exception(self):
        """
        APIRequestor().request() should raise specific exceptions
        based on the status code in the response
        """
        status_code_to_exception_class = [
            (400, exceptions.BadRequestError),
            (404, exceptions.BadRequestError),
            (429, exceptions.RateLimitError),
            (401, exceptions.AuthenticationError),
            (403, exceptions.PermissionError),
            (500, exceptions.GuidebookError),
            (502, exceptions.GuidebookError),
            (503, exceptions.GuidebookError),
        ]
        for status_code, expected_exception in status_code_to_exception_class:
            for method in ['get', 'put', 'post', 'patch', 'delete']:
                with mock.patch('guidebook.api_requestor.requests') as mock_requests:
                    getattr(mock_requests, method).return_value = mock.Mock(status_code=status_code)
                    with self.assertRaises(expected_exception):
                        api_requestor = APIRequestor(api_key='fake-api-key')
                        api_requestor.request(method=method, url='fake-url')
