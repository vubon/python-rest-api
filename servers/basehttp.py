import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

from recipes.urls import get_path

HOST_NAME = '127.0.1.1'
PORT_NUMBER = 9000


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_GET(self):
        status_code, response = get_path(self.path, self.command)
        self.respond(status_code, response)

    def do_POST(self):
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(data_string)
        status_code, response = get_path(self.path, self.command, data=data)

        self.respond(status_code, response)

    def do_DELETE(self):
        status_code, response = get_path(self.path, self.command)
        self.respond(status_code, response)

    do_PUT = do_POST

    def handle_http(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        content = json.dumps(data)
        return bytes(content, 'UTF-8')

    def respond(self, status_code, data=None):
        response = self.handle_http(status_code, data)
        self.wfile.write(response)


if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))
