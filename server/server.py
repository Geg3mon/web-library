from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from http import HTTPStatus
import json
import os
from router import routes

from models.library import Library

dir_path = os.path.dirname(os.path.realpath(__file__))


class HttpGetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        # self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-type", "application/json")
        self.end_headers()
        # self.wfile.write(open(dir_path + '/templates/home.html', 'r').read().encode())
        self.wfile.write(json.dumps({'server_name': 'Simple library web server', 'author': 'Yevhenii Hrybanov'}).encode())


def run(server_class=HTTPServer, handler_class=HttpGetHandler):
    server_address = ('localhost', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

# my_library = Library('Ukraine', '3700', [], [])

if __name__ == "__main__":
    run()
