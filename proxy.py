import http.server
import json
import urllib.request

PORT = 8000
TARGET_URL = "https://openrouter.ai/api"

class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        
        path = self.path.replace('/v1/v1/', '/v1/')
        if path.startswith('/v1/messages'):
            path = '/v1/messages'
            
        try:
            data = json.loads(body)
            if 'model' in data:
                data['model'] = "deepseek/deepseek-chat"
            if 'max_tokens' in data and data['max_tokens'] > 4000:
                data['max_tokens'] = 4000
            modified_body = json.dumps(data).encode('utf-8')
        except Exception:
            modified_body = body
            
        headers = {}
        for key, value in self.headers.items():
            if key.lower() not in ['host', 'content-length', 'content-encoding', 'transfer-encoding']:
                headers[key] = value
                
        full_url = TARGET_URL + path
        req = urllib.request.Request(full_url, data=modified_body, headers=headers, method='POST')
        
        try:
            with urllib.request.urlopen(req) as resp:
                self.send_response(resp.status)
                for header, value in resp.headers.items():
                    if header.lower() not in ['transfer-encoding', 'content-encoding']:
                        self.send_header(header, value)
                self.end_headers()
                self.wfile.write(resp.read())
        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self.end_headers()
            self.wfile.write(e.read())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode('utf-8'))

    def do_GET(self):
        path = self.path.replace('/v1/v1/', '/v1/')
        headers = {}
        for key, value in self.headers.items():
            if key.lower() not in ['host']:
                headers[key] = value
        req = urllib.request.Request(TARGET_URL + path, headers=headers, method='GET')
        try:
            with urllib.request.urlopen(req) as resp:
                self.send_response(resp.status)
                for header, value in resp.headers.items():
                    self.send_header(header, value)
                self.end_headers()
                self.wfile.write(resp.read())
        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self.end_headers()
            self.wfile.write(e.read())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode('utf-8'))

if __name__ == '__main__':
    server = http.server.HTTPServer(('127.0.0.1', PORT), ProxyHandler)
    server.serve_forever()
