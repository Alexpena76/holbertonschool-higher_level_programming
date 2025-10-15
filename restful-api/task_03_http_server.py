import http.server
import socketserver
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for our simple API server.
    Handles GET requests for different endpoints.
    """
    
    def do_GET(self):
        """
        Handle GET requests based on the requested path.
        Routes requests to different endpoints.
        """
        
        if self.path == '/':
            # Root endpoint - send simple text response
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            
        elif self.path == '/data':
            # Data endpoint - serve JSON data
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Create sample data
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            
            # Convert dictionary to JSON string and send
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode('utf-8'))
            
        elif self.path == '/status':
            # Status endpoint - return API status
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
            
        elif self.path == '/info':
            # Info endpoint - return API information
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            
            json_info = json.dumps(info)
            self.wfile.write(json_info.encode('utf-8'))
            
        else:
            # Handle undefined endpoints - return 404
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            error = {
                "error": "Endpoint not found",
                "message": f"The endpoint '{self.path}' does not exist"
            }
            
            json_error = json.dumps(error)
            self.wfile.write(json_error.encode('utf-8'))
    
    def log_message(self, format, *args):
        """
        Override to customize log messages.
        This is optional but helpful for debugging.
        """
        print(f"[{self.log_date_time_string()}] {format % args}")


def run_server(port=8000):
    """
    Start the HTTP server on the specified port.
    
    Args:
        port (int): Port number to run the server on (default: 8000)
    """
    
    # Create the server
    with socketserver.TCPServer(("", port), SimpleAPIHandler) as httpd:
        print(f"Server running on port {port}...")
        print(f"Access the API at: http://localhost:{port}")
        print(f"Available endpoints:")
        print(f"  - http://localhost:{port}/")
        print(f"  - http://localhost:{port}/data")
        print(f"  - http://localhost:{port}/status")
        print(f"  - http://localhost:{port}/info")
        print(f"\nPress Ctrl+C to stop the server")
        
        try:
            # Start serving requests
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped by user")


if __name__ == "__main__":
    run_server(8000)
