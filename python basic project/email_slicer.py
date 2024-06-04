def main():
    print("welcome to the email slicer")
    print("")
    
    email_input = input("input your email address: ")
    (username,domain) = email_input.split("@")
    (domain,extension) = domain.split(".")
    
    print(" the username is : ", username)
    print(" the domain is : ", domain)
    print(" the extension is : ", extension)


main()
    


#pratikdevkota

name = "pratik devkota"
(firstname,lastname)= name.split(" ")
print("first name is : ",firstname)
print("last name is : ",lastname)