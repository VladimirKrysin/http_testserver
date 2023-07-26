from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        if self.path == '/gribok':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write('<html><head><meta charset="utf-8">'.encode())
            self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
            self.wfile.write('<body>Привет, грибок!</body></html>'.encode())
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write('<html><head><meta charset="utf-8">'.encode())
            self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
            self.wfile.write('<body>Главная страница!</body></html>'.encode())


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('GG WP')
        httpd.server_close()


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    run(handler_class=HttpGetHandler)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
