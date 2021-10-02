from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
import pandas as pd
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
                datos = {}
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

            data_name = pd.read_csv('Name.csv')
            data_age = pd.read_csv('Age.csv')
            data_city = pd.read_csv('City.csv')

            data_name = data_name.append({'Key' : user_m2[0], 'Name' : user_m2[1], 'Num' : len(data_name.index)}, ignore_index=True)
            data_name = data_name.to_csv('Name.csv', index=False)

            data_age = data_age.append({'Key' : user_m2[0], 'Age' : user_m2[2], 'Num' : len(data_age.index)}, ignore_index=True)
            data_age = data_age.to_csv('Age.csv', index=False)

            data_city = data_city.append({'Key' : user_m2[0], 'City' : user_m2[3], 'Num' : len(data_city.index)}, ignore_index=True)
            data_city = data_city.to_csv('City.csv', index=False)

def main():
    
    
    server = HTTPServer(('', serverVariables.PORT), Servidor)
    print("Servidor corriendo en el puerto", serverVariables.PORT)
    server.serve_forever()

    
if __name__ == '__main__':
    main()