import http.server
import socketserver

# Settings
HOST = "0.0.0.0"  # Listen on all available network interfaces
PORT = 8080       # You can change this if you want

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Override to make logging cleaner
        print(f"[SERVER] {self.address_string()} - {format % args}")

# Threading for better performance
with socketserver.ThreadingTCPServer((HOST, PORT), Handler) as httpd:
    print(f"🚀 Server running at http://{HOST}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server shutting down...")
        httpd.shutdown()
