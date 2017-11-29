import requests

from guidebook import exceptions


class APIRequestor(object):

    def __init__(self, api_key):
        self.api_key = api_key

    def request(self, method, url, data=None, params=None):
        """
        Given a HTTP method, a url, request body data, and
        url query params, makes the request to the guidebook
        API and returns the JSON response body loaded into
        python. Raises on bad network conditions, bad arguments,
        or an error returned by the Guidebook API
        """
        requests_kwargs = {
            'url': url,
            'data': data,
            'params': params,
            'headers': {'Authorization': 'JWT ' + self.api_key},
        }
        try:
            response = getattr(requests, method)(**requests_kwargs)
        except Exception as e:
            message = ('Unexpected network error. A {} was raised with '
                       'message {}'.format(type(e).__name__, str(e)))

            # catch *any* Exception so that if requests fails for any reason
            # (bad network conditions, bad python arguments etc.), we raise
            # a GuidebookError instance
            raise exceptions.GuidebookError(message)

        interpreted_response = self.interpret_response(response)
        return interpreted_response

    def interpret_response(self, response):
        """
        Return the JSON data in the response body laoded into
        python. Raises if the response body isn't valid JSON
        or response status_code indicates that an error occurred
        """
        try:
            response_json = response.json()
        except (ValueError, TypeError):
            message = ('Invalid response body from API: {}. Status code: '
                       '{}'.format(response.content, response.status_code))
            raise exceptions.GuidebookError(message)

        # if the request wasn't successful, raise an appropriate
        # exception
        if not (200 <= response.status_code < 300):
            if response.status_code == 429:
                raise exceptions.RateLimitError(response.json())
            elif response.status_code in [400, 404]:
                raise exceptions.BadRequestError(response.json())
            elif response.status_code == 401:
                raise exceptions.AuthenticationError(response.json())
            elif response.status_code == 403:
                raise exceptions.PermissionError(response.json())
            else:
                raise exceptions.GuidebookError(response.json())

        return response_json
