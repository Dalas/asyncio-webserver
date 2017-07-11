from mixins import HeadersParserMixin


class Application(HeadersParserMixin):
    def __init__(self, routes):
        pass

    async def process_request(self, reader):
        headers = await self.parse_headers(reader)

        print(headers)

        response = b"HTTP/1.1 200 OK\r\n"
        response += b"Date: Mon, 27 Jul 2009 12:28:53 GMT\r\n"
        response += b"Server: Apache/2.2.14 (Win32)\r\n"
        response += b"Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT\r\n"
        # writer.write("Content-Length: 88\r\n".encode('utf-8'))
        response += b"Content-Type: text/html\r\n"
        response += b"\r\n"
        response += br"<html><body><h1>Hello, World!</h1></body></html>"

        return response


