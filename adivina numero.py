# importing random
from random import *

# taking input from user
user_pass = input("Ponga su contraseña")

# storing alphabet letter to use thm to crack password
password = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]

# initializing an empty string
guess = ""

# using while loop to generate many passwords untill one of
# them does not matches user_pass
count=0
while (guess != user_pass):
    guess = " "
    # generating random passwords using for loop
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0, 9)]
        guess = str(guess_letter) + str(guess)
    # printing guessed passwords
    print(guess)
    count += 1

# printing the matched password
print("Su contraseña es:", guess)
print(count)