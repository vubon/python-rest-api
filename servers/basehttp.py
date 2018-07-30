import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

from recipes.urls import paths
from recipes.views import all_recipes

HOST_NAME = 'localhost'
PORT_NUMBER = 9000

TODOS = [
    {'id': 1, 'title': 'learn python'},
    {'id': 2, 'title': 'get paid'},
]


def test():
    print('Hell Path')


def recipes():
    a = [{'id': 1, 'name': 'test recipe'}]
    return a


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_GET(self):
        # paths = {
        #     '/': {'status': 200, 'data': ''},
        #     '/foo': {'status': 200, 'data': TODOS},
        #     '/bar': {'status': 302},
        #     '/baz': {'status': 404},
        #     '/qux': {'status': 500}
        # }

        if self.path in paths:
            if self.path == '/recipes':
                a = all_recipes()
                self.respond(200, a)
            else:
                self.respond(200)
                test()
        else:
            self.respond(404)

    def do_POST(self):
        request_path = self.path
        print(request_path)
        self.send_response(201)
        self.send_header('Content_type', 'application/json')
        self.end_headers()
        return

    do_PUT = do_POST
    do_DELETE = do_GET

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
