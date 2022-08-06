from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
import json
import os
from urllib.parse import parse_qs, unquote
from models.library import my_library
from router import routes



dir_path = os.path.dirname(os.path.realpath(__file__))

route = json.dumps(routes)


class HttpGetHandler(BaseHTTPRequestHandler):

    def _set_headers_200(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _set_headers_404(self):
        self.send_response(HTTPStatus.NOT_FOUND)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _set_headers_405(self):
        self.send_response(HTTPStatus.METHOD_NOT_ALLOWED)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        for obj in routes:
            if self.path == "/main" and self.command == "GET":
                self.send_response(HTTPStatus.OK)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(
                    open(dir_path + '/templates/main.html', 'r').read().encode())
                break

            elif obj["path"] == self.path and obj["method"] == self.command:
                self._set_headers_200()
                json_data = obj["call"]
                self.wfile.write(json_data.encode())
                print(json_data)
                break

            elif obj["path"] == self.path and obj["method"] != self.command:
                self._set_headers_405()
                self.wfile.write(json.dumps(
                    {'status': '405',
                     'description': 'Method not allowed'}).encode())
                break

        if not self.path == "/main" and (next((x for x in routes if x["path"] == self.path), None)) == None:
            self._set_headers_404()
            self.wfile.write(json.dumps(
                {'status': '404',
                 'description': 'Page not found'}).encode())

    def do_POST(self):
        for obj in routes:
            if obj["path"] == self.path and obj["method"] == self.command:
                self._set_headers_200()
                length = int(self.headers.get('content-length'))
                field_data = (self.rfile.read(length))
                fields = parse_qs(field_data.decode())
                for k, v in fields.items():
                    fields[k] = unquote(v[0])
                data = json.dumps(fields)
                self.wfile.write(obj['call'].encode())
                print(f'{fields}')
                print(f'{data}')
                print(my_library.library_books_list())
                break

            elif obj["path"] == self.path and obj["method"] != self.command:
                self._set_headers_405()
                self.wfile.write(json.dumps(
                    {'status': '405', 'description':
                     'Method not allowed'}).encode())
                break

        if (next((x for x in routes if x["path"] == self.path), None)) == None:
            self._set_headers_404()
            self.wfile.write(json.dumps(
                {'status': '404',
                 'description': 'Page not found'}).encode())


def run(server_class=HTTPServer, handler_class=HttpGetHandler):
    server_address = ('localhost', 8000)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server at http://localhost:8000\nPress CTRL+C to shutdown')

    try:
        httpd.serve_forever()
        
    except KeyboardInterrupt:
        httpd.server_close()
        print(f'\n\n _===============_ \n| Shutdown server |\n =================\n')
    
    
if __name__ == "__main__":
    run()
