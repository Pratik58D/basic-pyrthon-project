import random
user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    
    
    if user_input == "q":
        break
        
    if user_input not in options:
        continue
    
    computer_pick = random.choice(options)
    print("computer Picked: ",computer_pick)
    print("you picked: ",user_input)
    
    if user_input== computer_pick:
        print("Its draw!")
       
    
    elif user_input== "rock" and computer_pick== "scissors" :
        print("you win!")
        user_wins +=1
       
    elif user_input== "paper" and computer_pick== "rock" :
        print("you win!")
        user_wins +=1
        
    
    elif user_input== "scissors" and computer_pick== "paper" :
        print("you win!")
        user_wins +=1
         
 
        
    else:
        print("you lose! ")
        computer_wins +=1
    

print("you won ",user_wins ,"times")
print("computer won ",computer_wins, "times")
print("goodbye!")
    
    
        
    