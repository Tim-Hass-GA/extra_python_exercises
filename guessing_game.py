# Guessing Game

# Create a program that asks the user to guess a number between 1 and 100.

# Once the user guesses a number, the program should say, higher, lower, or
# tell the user that he got the number correct. The user should continue to
# make guesses until he guesses correctly. Also, once the user guesses correctly,
# the program should print the number of guesses needed to arrive at the correct answer.

# Below is sample output:

# Guess a number between 1 and 100
# 50 <-- user input
# The number is lower than 50.  Guess again
# 25
# The number is lower than 25.  Guess again
# 13
# The number is higher than 13.  Guess again
# 20
# The number is lower than 20.  Guess again
# 17
# The number is higher than 17.  Guess again
# 18
# The number is higher than 18.  Guess again
# 19
# You got it in 7 tries

# HINT:
# To get input from a user use the input() method:
# num_of_cookies = input("How many cookies should I eat?")
# num = int(num)

# This will assign the typed input value to your variable as a number

# *** your code here ***

################

import random
random.random()
num = random.randint(1,10)
print(num)
count = 0
guess = int(input("Guess a number"))
found = False

while(found == False):
  if (guess == num):
    found = True
    count += 1
    print("yeah",guess,"is equal to",num,"found in",count,"attemps")
  else:
    count += 1
    if (guess > num):
      print("Incorrect",guess,"is greater than the secret number and this is your",count,"attempt")
    elif (guess < num):
      print("Incorrect",guess,"is less than then the secret number and this is your",count,"attempt")
    guess = int(input("guess again"))

################
