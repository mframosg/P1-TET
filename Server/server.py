from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import serverVariables
import json
import requests


class Servidor(BaseHTTPRequestHandler):
    def do_POST(self):
        url = urlparse(self.path)
        path = url.path

        if (path == '/create'):
            length = int(self.headers.get('content-length'))
            field_data = self.rfile.read(length)
            entry = json.loads(field_data.decode('utf-8'))
            header = {'content-type': 'application/json'}
            
            to_send = {'key': entry['id'], 'value': entry['name']}
            requests.post(serverVariables.NAME_SERVER, data=to_send, headers=header)
            
            to_send = {'key': entry['id'], 'value': entry['age']}
            requests.post(serverVariables.AGE_SERVER, data=to_send, headers=header)
            
            to_send = {'key': entry['id'], 'value': entry['city']}
            requests.post(serverVariables.CITY_SERVER, data=to_send, headers=header)

            to_send = {'key': entry['id'], 'value': entry['score']}
            requests.post(serverVariables.SCORE_SERVER, data=to_send, headers=header)

            self.send_response(201)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(str(to_send), 'utf-8'))
        else:
            res = { "error": { "code": 404, "message": "404 Resource Not Found" } }
            self.send_response(404)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(str(res), 'utf-8'))
        
    # def do_GET(self):
    #     url = "http://"


def main():
    server = HTTPServer(('', serverVariables.PORT), Servidor)
    print("Servidor corriendo en el puerto", serverVariables.PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
