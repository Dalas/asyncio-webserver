

class Request(object):
    def __init__(self, raw_request):
        self._request = raw_request.decode()
        self._raw_request = raw_request

    @staticmethod
    async def initialize(reader):
        # TODO: rewrite headers reader

        raw_request = await reader.readline()

        if raw_request == b'':
            raise Exception('Test')

        while not reader.at_eof():
            line = await reader.readline()

            # TODO: remove this
            if line == b'\r\n':
                break

            raw_request += line

        return Request(raw_request)

    @property
    def request(self):
        return self._request
