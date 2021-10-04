from json.encoder import py_encode_basestring_ascii
import requests
import clientVariables
from os import system, name

valid_commands = ["help", "add", "get", "list"]
if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')

while(True): #tet

    print("\nWelcome to our distributed database system for our advanced networking class.\n")
    print("Data is stored as <key,value>.\n It will contain this parameters: <unique key,(Name,Age,City)>\n")
    print("Example -->  <smaring1,(Simon,21,Medellin)>")
    print("\nEach command will guide you through the process\n")
    print("\nList of available commands:")
    print("add")
    print("get")
    print("list")
    print("\nSyntax: tet <command>\n")
    print("Type enter, then follow the instructions.")

    def input_command():
        choice=input("Enter a command (or enter q to quit): ")
        if choice.startswith('tet') and choice.split()[1] in valid_commands:
            choice = choice.split()
            return choice
        elif choice == 'q':
            quit()
        else:
            print("You must enter a valid command. Please try again.")
            input_command()
        return choice
    
    register = [] 
    command = input_command()
    if command.split()[1] == "add":
        cur = ""
        while not cur.isnumeric():
            cur = input("Enter you id (number): ")
            if not cur.isnumeric():
                print("You must enter a number.")
        register.append(cur)
        cur = input("Enter your name: ")
        register.append(cur)
        while not cur.isnumeric():
            cur = input("Enter your age (number): ")
            if not cur.isnumeric():
                print("You must enter a number.")
        register.append(cur)
        cur = input("Enter your city: ")
        register.append(cur)
        while not cur.isnumeric():
            cur = input("Enter your score (number): ")
            if not cur.isnumeric():
                print("You must enter a number.")
        register.append(cur)

        
    if command.split()[1] == "get":
        query = input("Enter the ID number of the register you want to find: ")
    if command.split()[1] == "list":
        pass #llamar a la función de listar o el procedimiento correspondiente
    

    #if(choice=="A"):
    #    equ=input("Ingresa tu <k,v>\n\n")

    #elif(choice=="C"):
    #    equ=input("Ingresa tu <k>\n\n")

    #

    #elif(choice=="X"):
    #    break
    
    url = 'http://127.0.0.1/create'



    datos = {
        'id': values[0], 
        'name': values[1], 
        'age': values[2], 
        'city': values[3], 
        'score': values[4],
    }

    header = {
        'content-type': 'application/json'
    }

    requests.post(url, data = datos, headers = header)

print("Bye!")