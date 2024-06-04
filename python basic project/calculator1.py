def add(a,b):
    answer = a + b
    return answer
def sub(a,b):
    answer = a - b
    return answer

def multiply(a,b):
    answer = a * b
    return answer
def divide(a,b):
    answer = a / b
    return answer

print("A. Sum. ")
print("B. Substraction. ")
print("C. Multiply. ")
print("D. Divide. ")
print("E. exit. ")

choice = input("enter your choice: ")

if choice == "a" or choice =="A":
    num1 = int(input("input the first number: "))
    num2 = int(input("input the second number: "))
    print("sum is : ", add(num1, num2))
    
if choice == "b" or choice =="B": 
    num1 = int(input("input the first number: "))
    num2 = int(input("input the second number: "))
    print("difference is : ",sub(num1, num2))
    
    
if choice == "c" or choice =="C":
    num1 = int(input("input the first number: "))
    num2 = int(input("input the second number: "))
    print("multiplication is : ",multiply(num1, num2))
    
    
if choice == "d" or choice =="D":
    num1 = int(input("input the first number: "))
    num2 = int(input("input the second number: "))
    print("multiplication is : ",divide(num1, num2))
        
if choice == "e" or choice =="E":
    print("quit the program")
    quit()
    

