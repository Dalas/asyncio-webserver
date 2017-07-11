from middlewares.RequestMiddleWares.BaseMiddleWare import BaseMiddleWare


class HeadersParserMiddleWare(BaseMiddleWare):

    @classmethod
    async def process_request(cls, request):
        # TODO: add checks
        headers = request.request.split('\r\n')

        request.header = headers.pop(0)

        cls.process_main_header(request)
        cls.process_headers(request, headers)

    @classmethod
    def process_main_header(cls, request):
        request_type, url, protocol = request.header.split(' ')

        request.type = request_type
        request.url = url
        request.protocol = protocol

    @classmethod
    def process_headers(cls, request, headers):
        request.headers = {}

        for header in headers:
            if header == '':
                continue

            k, v = header.split(':', 1)
            request.headers[k] = v[1:]
