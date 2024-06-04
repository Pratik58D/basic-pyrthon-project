# a dictionary that stores questions an answer
# have a variable that tracks the score of player
#loop through the dictionary using the key values pairs
#display each question to the user and allow them to answer 
#tell them if the are right or wrong
#show the final result when quitz is complete


quiz = {
    "question1": {
        "question":"Who developed Python Programming Language?",
        "answer": "Guido van Rossum",
    },
    "question2": {
        "question":"Is Python case sensitive when dealing with identifiers?",
        "answer": "yes",
    },
    "question3": {
        "question":"Which keyword is used for function in Python language?",
        "answer": "def",
    },
    "question4": {
        "question":"Which character is used to give single-line comments in Python?",
        "answer": "#",
    },
    "question5": {
        "question":" What does pip stand for python?",
        "answer": "Preferred Installer Program",
    },
    "question6": {
        "question":"which language is Python written?",
        "answer": "C",
    },
    "question7": {
        "question":" What do we use to define a block of code in Python language?",
        "answer": "Indentation",
    },
    "question8": {
        "question":"which one is mutable list or tuple",
        "answer": "def",
    },
    
}

score = 0 

for key,value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")
    
    if answer.lower() == value['answer'].lower():
        print('correct')
        score = score + 1
        print("your score is: "+ str(score))
        
    else:
        print("wrong! ")
        print("The answer is : "+ value['answer'])
        print("your score is: " + str(score))



        
print("your total score is: " + str(score))
        