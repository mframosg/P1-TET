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
    print("Input <key,value> must meet the following pattern <unique key,(Name,Age,City)>\n")
    print("Example -->  <smaring1,(Simon,21,Medellin)>")
    print("\nList of available commands:")
    print("add <key,value>")
    print("get <key>")
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
            cur = input("Enter you id: ")
            if not cur.isnumeric():
                print("You must enter a number.")
        register.append(cur)
        cur = input("Enter your name: ")
        register.append(cur)
        while not cur.isnumeric():
            cur = input("Enter your age: ")
            if not cur.isnumeric():
                print("You must enter a number.")
        register.append(cur)
        cur = input("Enter your city: ")
        register.append(cur)
        while not cur.isnumeric():
            cur = input("Enter your score: ")
            if not cur.isnumeric():
                print("You must enter a number.")
        register.append(cur)

        
    if command.split()[1] == "get":
        k = command[3:].replace(" ", "")
        values = k.replace("<", "").replace(">", "").replace("(", "").replace(")", "").split(",")
    if command.split()[1] == "list":
        pass #llamar a la función de listar o el procedimiento correspondiente
    
    url = 'http://127.0.0.1:8006/create'



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