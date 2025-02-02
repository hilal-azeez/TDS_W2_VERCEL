import json
from http.server import BaseHTTPRequestHandler

# Example data with marks of 100 students
student_marks = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92,
    "David": 88,
    # Add more students and their marks...
}

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query parameters
        params = self.parse_query_string(self.path)
        names = params.get('name', [])
        
        # Fetch the marks for each name
        marks = [student_marks.get(name, None) for name in names]

        # Prepare the response
        response = json.dumps({"marks": marks})
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(response.encode())

    def parse_query_string(self, url):
        """Helper function to parse the query string"""
        import urllib.parse
        parsed_url = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(parsed_url.query)
        return {k: v[0] for k, v in params.items()}

def handler(event, context):
    return RequestHandler(event, context)
