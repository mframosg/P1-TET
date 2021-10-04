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
            
            to_send = {"key": entry['id'], "value": entry['name']}
            to_send = str(to_send).replace('\'',"\"")
            requests.post(serverVariables.NAME_SERVER, data=str(to_send), headers=header)
            
            to_send = {"key": entry['id'], "value": entry['age']}
            to_send = str(to_send).replace('\'',"\"")
            requests.post(serverVariables.AGE_SERVER, data=to_send, headers=header)
            
            to_send = {"key": entry['id'], "value": entry['city']}
            to_send = str(to_send).replace('\'',"\"")
            requests.post(serverVariables.CITY_SERVER, data=to_send, headers=header)

            to_send = {"key": entry['id'], "value": entry['score']}
            to_send = str(to_send).replace('\'',"\"")
            requests.post(serverVariables.SCORE_SERVER, data=to_send, headers=header)

            res = { "succesfully": { "code": 201, "message": "User succesfully added" } }
            self.send_response(201)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(str(res), 'utf-8'))
        else:
            res = { "error": { "code": 404, "message": "404 Resource not found" } }
            self.send_response(404)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(str(res), 'utf-8'))

    def do_GET(self):
        url = urlparse(self.path)
        path = url.path
        if(path.find("/consult/") == 0 ):
            id = path[9:]
            url = f"http://127.0.0.1:8007/{id}"
            r = requests.get(url)
            data = r.text
            data = data.replace("{","").replace("}","").replace("\'","")
            data = data.split(":")

            url = f"http://127.0.0.1:8008/{id}"
            r = requests.get(url)
            data1 = r.text
            data1 = data1.replace("{","").replace("}","").replace("\'","")
            data1 = data1.split(":")
            

            url = f"http://127.0.0.1:8009/{id}"
            r = requests.get(url)
            data2 = r.text
            data2 = data2.replace("{","").replace("}","").replace("\'","")
            data2 = data2.split(":")

            url = f"http://127.0.0.1:8010/{id}"
            r = requests.get(url)
            data3 = r.text
            data3 = data3.replace("{","").replace("}","").replace("\'","")
            data3 = data3.split(":")

            dic = {data[0]:data[1], data1[0]:data1[1],data2[0]:data2[1], data3[0]:data3[1]}
            
            self.send_response(r.status_code)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(str(dic), 'utf-8'))
        else:
            res = { "error": { "code": 404, "message": "404 Resource not found" } }
            self.send_response(404)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(str(res), 'utf-8'))


def main():
    server = HTTPServer(('', serverVariables.PORT), Servidor)
    print("Servidor corriendo en el puerto", serverVariables.PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
