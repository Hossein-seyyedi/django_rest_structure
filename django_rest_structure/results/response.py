from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from .codes import ResultMessageStructure


class ResponseStructure:
    def __init__(self, message: ResultMessageStructure, body=None, err=None):
        self.message = message
        self.body = body
        self.err = err


class Request:
    def __init__(self, request: WSGIRequest):
        self.request = request
        self.err = None

    def get_request_data_info(self):
        pass

    @staticmethod
    def generate_response_data(response: ResponseStructure):
        http_response = JsonResponse({
            'status': {
                'code': response.message.code,
                'message': response.message.message,
                'is_success': response.message.is_success_result,

            },
            'result': response.body
        })

        http_response.err = response.err
        return http_response


def response_handler_dec(func):
    def wrapper(*args, **kwargs):
        return Request.generate_response_data(func(*args, *kwargs))

    return wrapper
