from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {
            "echo": "Hello from " + self.server.server_name, # pyright: ignore[reportAttributeAccessIssue]
            "path": self.path
        }
        self.wfile.write(json.dumps(response).encode())

server = HTTPServer(('0.0.0.0', 8080), EchoHandler)
server.serve_forever()