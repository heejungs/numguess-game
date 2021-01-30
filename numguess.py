# Author : LeeHyungi0622
# Issue : #2
# Date : 2021/01/30 

# Get name from user.
import random 

# Auto-generate the answer
answer = random.randint(1,100)
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
    # To concatenate the answer value with prompt message, casting the answer value as string value.
	print("That's not what I wanted!! The answer was ", str(answer))