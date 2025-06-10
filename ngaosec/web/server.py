from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os
import socket
from pathlib import Path

class NgaoSecRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Set the directory to serve files from
        web_dir = Path(__file__).parent / 'templates'
        super().__init__(*args, directory=str(web_dir), **kwargs)
    
    def do_GET(self):
        # Route requests to the appropriate handler
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

def start_server():
    # Create server
    server_address = ('127.0.0.1', 9090)
    
    # Check if port is available
    if is_port_in_use(9090):
        print(f"Port 9090 is already in use")
        return
    
    httpd = ThreadingHTTPServer(server_address, NgaoSecRequestHandler)
    print(f"Starting web server on http://{server_address[0]}:{server_address[1]}")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0
