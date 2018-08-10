import time
from http.server import HTTPServer

from servers.server import MyHandler

PORT = 5000


if __name__ == '__main__':
    httpd = HTTPServer(('', PORT), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % ('', PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % ('', PORT))
