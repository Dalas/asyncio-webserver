from middlewares import HeadersParserMiddleWare

from Request import Request

import asyncio


class Application(object):
    request_middlewares = (
        HeadersParserMiddleWare(),
    )

    def __init__(self, loop, routes, settings):
        self._loop = loop or asyncio.get_event_loop()
        self._server = self.create_server(settings)

    def create_server(self, settings):
        host = settings['host'] if 'host' in settings else '127.0.0.1'
        port = settings['port'] if 'port' in settings else 8888

        return asyncio.start_server(self.handle_connection, host=host, port=port)

    async def handle_connection(self, reader, writer):
        peername = writer.get_extra_info('peername')
        print('Accepted connection from {}'.format(peername))

        try:
            response = await self.handle_request(reader, writer)
            writer.write(response)
        except Exception as e:
            # TODO: return error and traceback here
            print(e)

        print('asd')

        writer.close()

    def start(self, and_loop=True):
        self._server = self._loop.run_until_complete(self._server)
        if and_loop:
            self._loop.run_forever()

    def stop(self, and_loop=True):
        self._server.close()
        if and_loop:
            self._loop.close()

    async def handle_request(self, reader, writer):
        request = await Request.initialize(reader)

        await self.process_request(request)

        response = b"HTTP/1.1 200 OK\r\n"
        response += b"Date: Mon, 27 Jul 2009 12:28:53 GMT\r\n"
        response += b"Server: Apache/2.2.14 (Win32)\r\n"
        response += b"Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT\r\n"
        # writer.write("Content-Length: 88\r\n".encode('utf-8'))
        response += b"Content-Type: text/html\r\n"
        response += b"\r\n"
        response += br"<html><body><h1>Hello, World!</h1></body></html>"

        return response

    async def process_request(self, request):
        for middleware in self.request_middlewares:
            await middleware.process_request(request)


