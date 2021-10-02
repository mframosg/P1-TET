from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import serverVariables

class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        #self.wfile.write(self.path[1:].encode())

        user = str(self.path[1:]).split("/")
        print(user)
        
        #2self.wfile.write(command)
        
        if user[0] == "X":
            self.wfile.write("X".encode())
            #break
        elif user[0] == "A":
            user_m = user[1].replace("<","").replace(">","").replace("(","").replace(")","").replace(" ","")

            user_m2 = user_m.split(",") # {}
            try:
                datos = {} # Diccionario de datos que devuelve Miguel
                names_file = open("Nombres.json", "r+")
                names_text = names_file.read().replace("\n","")
                names_data = json.loads(names_text)
                names_data.update({datos['id']: datos['name']})
                names_write = json.dumps(names_data)
                names_file.write(names_write)

                ages_file = open("Edades.json", "r+")
                ages_text = ages_file.read().replace("\n","")
                ages_data = json.loads(ages_text)
                ages_data.update({datos['id']: datos['age']})
                ages_write = json.dumps(ages_data)
                ages_file.write(ages_write)

                cities_file = open("Ciudades.json", "r+")
                cities_text = cities_file.read().replace("\n","")
                cities_data = json.loads(cities_text)
                cities_data.update({datos['id']: datos['city']})
                cities_write = json.dumps(cities_data)
                cities_file.write(cities_write)

                scores_file = open("Puntajes.json", "r+")    
                scores_text = scores_file.read().replace("\n","")
                scores_data = json.loads(scores_text)
                scores_data.update({datos['id']: datos['score']})
                scores_write = json.dumps(scores_data)
                scores_file.write(scores_write)
            except:
                pass


def main():
    server = HTTPServer(('', serverVariables.PORT), Servidor)
    print("Servidor corriendo en el puerto", serverVariables.PORT)
    server.serve_forever()

    
if __name__ == '__main__':
    main()