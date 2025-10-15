import http.server
import socketserver
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for a simple API server.
    """
    
    def do_GET(self):
        """
        Handle GET requests based on the requested path.
        """
        
        if self.path == '/':
            # Root endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            
        elif self.path == '/data':
            # Data endpoint - serve JSON data
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode('utf-8'))
            
        elif self.path == '/status':
            # Status endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
            
        else:
            # Handle undefined endpoints - return 404
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            error_response = {
                "error": "Endpoint not found"
            }
            
            json_error = json.dumps(error_response)
            self.wfile.write(json_error.encode('utf-8'))


def run_server(port=8000):
    """
    Start the HTTP server on the specified port.
    """
    
    with socketserver.TCPServer(("", port), SimpleAPIHandler) as httpd:
        print(f"Server running on port {port}...")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped by user")


if __name__ == "__main__":
    run_server(8000)
