
master_pwd = input("Enter the master Password: ")

def view():
    pass


def new():
    name = input ("Account name:  ")
    pwd = input("Password: ")
    # a is append mode there are read =r,write=w mode as well 
    
    with open('passwords.txt' , 'a') as f:
        f.write(name+ "|" +pwd + "\n")
        
        

while True:
    mode = input("Would you like to add a new password or view existing password(view,new)?.Press q to quit. ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "new":
        new()
    else:
        print("invalid mode. ")
        continue
        
        
        