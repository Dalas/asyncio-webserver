import asyncio
import logging
import concurrent.futures
import datetime
import random
import Application


def handler(reader, writer):
    return 123

a = Application.Application([])


class EchoServer(object):
    """Echo server class"""
    number = 0

    def get_number(self):
        self.number += 1
        return self.number

    def __init__(self, host, port, loop=None):
        self._loop = loop or asyncio.get_event_loop()
        self._server = asyncio.start_server(self.handle_connection, host=host, port=port)

    def start(self, and_loop=True):
        self._server = self._loop.run_until_complete(self._server)
        logging.info('Listening established on {0}'.format(self._server.sockets[0].getsockname()))
        if and_loop:
            self._loop.run_forever()

    def stop(self, and_loop=True):
        self._server.close()
        if and_loop:
            self._loop.close()

    # @asyncio.coroutine
    # def handle_connection(self, reader, writer):
    #     peername = writer.get_extra_info('peername')
    #
    #     headers = yield from a.parse_headers(reader)
    #     print(headers)
    #
    #     logging.info('Accepted connection from {0} {1}'.format(
    #         peername,
    #         datetime.datetime.now().strftime("%H:%m:%s"),
    #     ))
    #
    #     writer.write("HTTP/1.1 200 OK\r\n".encode('utf-8'))
    #     writer.write("Date: Mon, 27 Jul 2009 12:28:53 GMT\r\n".encode('utf-8'))
    #     writer.write("Server: Apache/2.2.14 (Win32)\r\n".encode('utf-8'))
    #     writer.write("Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT\r\n".encode('utf-8'))
    #     writer.write("Content-Length: 88\r\n".encode('utf-8'))
    #     writer.write("Content-Type: text/html\r\n".encode('utf-8'))
    #     writer.write("\r\n".encode('utf-8'))
    #     writer.write(r"<html><body><h1>Hello, World!</h1></body></html>".encode('utf-8'))
    #
    #     logging.info('Finish processing {0}'.format(
    #         datetime.datetime.now().strftime("%H:%m:%s")
    #     ))
    #
    #     writer.close()
    #     logging.info('closed')

    async def handle_connection(self, reader, writer):
        peername = writer.get_extra_info('peername')
        logging.info('Accepted connection from {}'.format(peername))

        # try:
        response = await a.process_request(reader)
        writer.write(response)
        # except Exception as e:
        #     print(e)

        print('asd')

        writer.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    server = EchoServer('127.0.0.1', 8888)
    try:
        server.start()
    except KeyboardInterrupt:
        pass  # Press Ctrl+C to stop
    finally:
        server.stop()
