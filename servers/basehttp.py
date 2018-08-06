import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

from recipes.urls import paths


HOST_NAME = '127.0.1.1'
PORT_NUMBER = 9000


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
        # print(self.path.split('/')[2])

        # if self.path == '/recipes':
        #     a = all_recipes()
        #     self.respond(200, a)
        #
        # elif self.path == '/recipes/{}'.format(self.path.split('/')[2]):
        #     pk = self.path.split('/')[2]
        #
        #     def get_data(pk):
        #         for data in all_recipes():
        #             if data['id'] == int(pk):
        #                 return [data]
        #         return []
        #
        #     self.respond(200, get_data(pk))
        #
        # else:
        #     self.respond(404)
        print(self.path)
        if any(self.path in url for url in paths):

            if self.path == '/':
                self.respond(paths[0][1].status_code, paths[0][1].data)

            elif self.path == '/recipes':

                self.respond(paths[1][1].status_code, paths[1][1].data)

            elif self.path == '/recipes/{}':
                pk = self.path.split('/')[2]
                print(paths[2])

                self.respond(paths[2][1].status_code, paths[2][1].data)

        else:
            self.respond(404, 'Not Found')

    def do_POST(self):
        request_path = self.path
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
