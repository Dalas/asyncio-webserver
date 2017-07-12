

class HeadersParserMixin(object):

    @classmethod
    async def parse_headers(cls, reader):
        headers = {}

        base_headers = await reader.readline()

        while not reader.at_eof():
            header = await reader.readline()

            header = header.decode('utf-8')

            # TODO: remove this
            if header == '\r\n':
                break

            k, v = header.split(":", 1)

            headers[k] = v[1: -2]

        return headers

    # @pa


