import requests
import clientVariables

while(True):

    print("\nBienvenido a nuestra Base de Datos Distribuida. Aqui podras guardar tus datos personales.\n")
    print("Todo sera muy sencillo para ti solo sigue las siguientes reglas:\n")
    print("Seguiremos el formato   <k,v>     <clave unica,(Nombre,Edad,Ciudad)>\n")
    print("Ejemplo--->  <cagiraldoa,(Cristian,19,Medellin)>\n")
    print("A para agregar\n")
    print("C para consulta de datos por <k>\n")
    print("B para borrar datos por <k>\n")
    print("X si no necesitas más de mi\n")

    decision=input("Que decides:   ")

    if(decision=="A"):
        equ=input("Ingresa tu <k,v>\n\n")

    elif(decision=="C"):
        equ=input("Ingresa tu <k>\n\n")

    

    elif(decision=="X"):
        break
    
    url = 'http://127.0.0.1/create'



    datos = {
        'id': '1001268576', 
        'name': 'Juansedo', 
        'age': '19', 
        'city': 'Salgar', 
        'score': '65'
    }

    header = {
        'content-type': 'application/json'
    }

    requests.post(url, data = datos, headers = header)

print("Bye!")