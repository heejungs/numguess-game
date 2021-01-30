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