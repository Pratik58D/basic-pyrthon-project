def add(a,b):
    answer = a + b
    print("The sum of numbers is : " , answer)
def sub(a,b):
    answer = a - b
    print("The difference of numbers is : " , answer)
def multiply(a,b):
    answer = a * b
    print("The multiplication of numbers is : " , answer)
def divide(a,b):
    answer = a / b
    print("the division of numbers is : " , answer)
    
print("A.Addition")
print("B.Substraction")
print("C.Multiplication")
print("D.Division")
print("E.Exit")

choice = input("input your choice: ")

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))
    add(a,b)
elif choice == "b" or choice == "B":
    print("Substraction")
    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))
    sub(a,b)
elif choice == "c" or choice == "C":
    print("MUltiplication")
    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))
    multiply(a,b)
elif choice == "d" or choice == "D":
    print("Division")
    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))
    divide(a,b)
elif choice == "e" or choice == "E":
    print("Exit the program")
    quit()
 

