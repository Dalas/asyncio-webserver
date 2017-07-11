

class BaseMiddleWare(object):
    def __init__(self):
        pass

    def process_request(self, request):
        return request

    def process_response(self, response):
        return response
