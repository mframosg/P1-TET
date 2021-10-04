from json.encoder import py_encode_basestring_ascii
import requests
import clientVariables
from os import system, name



def main():
    while(True): #tet

        
    
        choice=input("Enter a command (or enter q to quit): ")
        if choice in clientVariables.VALID_COMMANDS:
            print("You chose"+ choice) 
        elif choice == 'q':
            quit()
        else:
            print("You must enter a valid command. Please try again."+"\n")
            quit()
        
        register = [] 
        command = choice
        if command == "add":
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

            to_send = {"id": register[0], "name": register[1], "age": register[2], "city": register[3], "score": register[4]}
            to_send = str(to_send).replace('\'',"\"")
            requests.post(clientVariables.URL_ADD, data = to_send, headers = clientVariables.HEADER)

        elif command == "get":
            cur = ""
            while not cur.isnumeric():
                cur = input("Enter the id you want to search: ")
                if not cur.isnumeric():
                    print("You must enter a number.")
            r=requests.get(clientVariables.URL + cur)
            person = r.text.replace("}","").replace("{","").replace("\'","").split(',')
            print(f"The id {cur} that you search is from : "+"\n"+person[0]+"\n"+person[1]+"\n"+person[2]+"\n"+person[3])
            
    

if __name__ == '__main__':
    print("\nWelcome to our distributed database system for our advanced networking class.\n")
    print("\nList of available commands:")
    print("add")
    print("get")
    main()