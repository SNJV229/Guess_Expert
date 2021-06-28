# Problem Statement:-)
# Create a python program in which the user selects a particular range of number (example 20 to 80 or 330 to 430). 
# The system should automatically select some random number and the user must identify that number selected by the system 
# in minimum number of guesses.

# If the user identifies it in the required number of guesses then it should print 
# "Yeah! You identified the number".

# Else if the number guessed by the user is higher than the randomly selected number then it should print
# "Please try again! The number you guessed is too high".

# Else if he number guessed by the user is smaller than the randomly selected number then it should print
# "Please try again! The number you guessed is too small".

# Else if the user does not guess the integer in minimum number of guesses, then it should give 
# "Oops! All you chances are finished. Better luck next time!".

import random as rn
import math

L_lim = int(input("Enter the lower range: "))
U_lim = int(input("Enter the Higher range: "))

key = rn.randint(L_lim,U_lim)

print("\n Number of chance you get to guess the number is: ",round(math.log(U_lim - L_lim + 1, 2)))

counter = 0
 
while counter < math.log(U_lim - L_lim + 1, 2):
    counter += 1
    
    guess = int(input("\n Enter your %d number: " % counter))
    
    if key == guess:
        print("\n Yeah! You identified the number")
        break
    elif key>guess:
        print("\n Please try again! The number you guessed is too small")
    elif key<guess:
        print("\n Please try again! The number you guessed is too high")
        
if counter > math.log(U_lim - L_lim + 1, 2):
    print("\n Oops! All you chances are finished. Better luck next time!")