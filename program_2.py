# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
def simple_math():
    number1 = 453
    number2 = 781
print("453 + 781")
question = int(input("Add these two numbers and print your result: "))
answer = 453 + 781 
if question == 1234:
        print("Congratulations you are correct!")
else:
    print("The Correct answer was:", answer)
simple_math()