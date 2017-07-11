import asyncio
import logging
import concurrent.futures
import datetime
import random
from Application import Application


SETTINGS = {
    'port': 8888,
    'host': '127.0.0.1'
}


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    server = Application(loop, [], SETTINGS)

    try:
        server.start()
    except KeyboardInterrupt:
        pass  # Press Ctrl+C to stop
    finally:
        server.stop()
