import time
from http.server import HTTPServer

from servers.request import get_host
from servers.server import MyHandler

PORT = 5000


if __name__ == '__main__':
    httpd = HTTPServer((get_host(), PORT), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (get_host(), PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (get_host(), PORT))
