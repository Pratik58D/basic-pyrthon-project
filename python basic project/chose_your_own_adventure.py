name = input("Type your name: ")
print("Welcome",name,"to this adventure!")

answer = input("Your are on a dirt road,,it has come to an end and you can go left or right.which way would you like to go? ").lower()

if answer == "left":
    answer1 = input("Here is a two cave.Do you want to enter the first or second cave. Type first or second: ").lower()
    if answer1 == "first":
        print("you have eaten by bear")
    elif answer1 == "second" :
        print("There is a another two cave in the cave.choose left or right: ")
        answer3 = input("Left or right").lower()
        if answer3 == "left":
            print("There is tiger you lose.")
        elif answer3 == "right":
            print("There are two cave inside the cave: ")

elif  answer == "right":
    answer2 = input("There is two box here. choose one left or right: ").lower()
    if answer2 == "left":
        print("you got a gold")
    else:
        print("Here is a bomb.You lose")
else:
    print("Not a valid option.You lose. ")


