
import random

answer = random.randint(1,100)
#is it enough?
# Author : LeeHyungi0622
# Issue : #2
# Date : 2021/01/30 

# Get name from user.
# Auto-generate the answer
# Print prompt message and get the username from user.
username = input("Hi there, What's your name?? ")
# Print prompt message and get the guess number from user. 
guess = int(input("Hi, "+ username + "guess the number: "))

# Conditional statement
# Check the guess number whether it is equal to answer or not.
if guess == answer:
    # To concatenate the answer value with prompt message, casting the answer value as string value.
	print("Correct! The answer was ", str(answer))
else:
    # Make a hint for user ( up & down)
    if guess > answer:
        print("Incorrect!, enter lower number.")
    else:
        print("Incorrect!, enter higher number.")

