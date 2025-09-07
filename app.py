import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer


def main() -> None:
    port = int(os.environ.get("PORT", 8000))
    # Serve files from repo root
    handler = SimpleHTTPRequestHandler
    with TCPServer(("0.0.0.0", port), handler) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    main()


