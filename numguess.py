import random

answer = random.randint(1,100)

# Author : LeeHyungi0622
# Issue : #2
# Date : 2021/01/30 

# Get name from user.
# Auto-generate the answer
# Print prompt message and get the username from user.
username = input("Hi there, What's your name? ")
# Print prompt message and get the guess number from user. 

# Let user choose the number of chances.
chance = int(input("Hi, "+ username + " How many chances do you want? "))

# Conditional statement
# Check the guess number whether it is equal to answer or not.
# Repeat 'chance' times. 
for i in range(1, chance+1):
	guess = int(input("Guess the number(1-100): "))
	if guess == answer:
    	# To concatenate the answer value with prompt message, casting the answer value as string value.
		print("Correct! The answer was ", str(answer))
		break
	elif chance>i:
	# Formatted to show the chances left.
		print("Try again! You have {} time(s) left.".format(chance-i))
	else:
    	# To concatenate the answer value with prompt message, casting the answer value as string value.
		print("That's not what I wanted!! The answer was ", str(answer))
