# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

# Henry Forst
# October 2nd, 2025
# Assignment 5

import random
def simple_math():
#generate random #
    random_num1 = random.randint(1, 501)
    random_num2 = random.randint(1, 501)
    print(f"{random_num1} + {random_num2}")

    question = int(input("Add these two numbers and print your result: "))
    answer = random_num1 + random_num2
    if question == answer:
        print("Congratulations you are correct!")
    else:
        print("The Correct answer was:", answer)
simple_math()