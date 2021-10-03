from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import nodeVariables
import os
import json
class DBServer(BaseHTTPRequestHandler):

    def do_POST(self):
        url = urlparse(self.path)
        path = url.path

        if (path == '/create'):
            length = int(self.headers.get('content-length'))
            field_data = self.rfile.read(length)
            entry = json.loads(field_data.decode('utf-8'))

            fp = open('data.json', 'r')
            read = json.load(fp)
            read.append(entry)
            fp.close()

            f = open('data.json', 'w')
            json.dump(read, f)
            f.close()

    def do_GET(self):
        url = urlparse(self.path)
        path = url.path

        if(path.find("/") == 0 ):
            id = path[1:]
            fp = open('data.json', 'r')
            data = json.load(fp)
            ids = [d for d in data if id in d]
            if(len(ids) == 0):
                res = { "error": { "code": 404, "message": "404 Resource Not Found" } }
                self.send_response(404)
                self.send_header("content-type", "application/json")
                self.end_headers()
                self.wfile.write(bytes(str(res), nodeVariables.ENCODING_FORMAT))
            else:
                res={'nombre' : ids[0][id]}
                self.send_response(201)
                self.send_header("content-type", "application/json")
                self.end_headers()
                self.wfile.write(bytes(str(res), nodeVariables.ENCODING_FORMAT))


if __name__ == "__main__":
    webServer = HTTPServer(
        (nodeVariables.IP_SERVER, nodeVariables.PORT), DBServer)
    print("Server started http://%s:%s" %
          (nodeVariables.IP_SERVER, nodeVariables.PORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.\n")
