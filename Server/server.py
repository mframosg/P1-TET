from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
import pandas as pd
import serverVariables
from urllib.parse import urlparse, parse_qs


class Servidor(BaseHTTPRequestHandler):

    def do_GET(self):

        # self.send_response(200)
        # self.send_header('content-type', 'text/html')
        # self.end_headers()
        #self.wfile.write(self.path[1:].encode())
        # user = str(self.path[1:]).split("/")
        user = urlparse(self.path)
        path = user.path
        query = parse_qs(user.query)
        print (user)
        print(path)
        print(query)
        
        #2self.wfile.write(command)
        
               
        if user[0] == "X":
            self.wfile.write("X".encode())
            #break
        elif user[0] == "A":
            user_m = user[1].replace("<","").replace(">","").replace("(","").replace(")","").replace(" ","")

            user_m2 = user_m.split(",")

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