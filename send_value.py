import http.server
import socketserver

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', 'http://127.0.0.1:5500')  # Allow requests from this origin
        self.end_headers()
        self.wfile.write(b'hi') # Send the value "hi"

PORT = 8000

with socketserver.TCPServer(('', PORT), MyHandler) as httpd:
    print(f'Sending value "hi" to http://localhost:{PORT}') # URL where you need to send the value
    httpd.serve_forever()