import http.server
import json
from urllib.parse import urlparse


class BasicHandler(http.server.SimpleHTTPRequestHandler):
   

    def send_json_response(self, data=None, code=0, message="success"):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        json_data = json.dumps({
            "data": data,
            "code": code,
            "message": message
        })
        self.wfile.write(json_data.encode('utf-8'))

    def not_found_JSON(self):
        self.send_json_response(None, 1, "Not Found")
    
    
    def log(self):
        print('Method:', self.command)
        print('Path:', self.path)
