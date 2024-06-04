#generate random number
#track how many times user takes to guess

import random
top_of_range = int(input("Type a number: "))
guesses = 0

if top_of_range <= 0:
    print("Type number grewater than zero")
    quit()

random_number= random.randint(0,top_of_range)

while True:
    guesses +=1
    user_guess = int(input("make a guess: "))
    if user_guess == random_number:
        print("correct!")
        break
    elif  user_guess > random_number:
        print("you were above the number!")
        continue
    else:
        print("you were below the number")
        continue
    

print("total Guess are: ", guesses)