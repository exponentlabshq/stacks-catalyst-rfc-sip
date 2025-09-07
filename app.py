import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer


class RootHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/pre.html"
        return super().do_GET()


def main() -> None:
    port = int(os.environ.get("PORT", 8000))
    with TCPServer(("0.0.0.0", port), RootHandler) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    main()


