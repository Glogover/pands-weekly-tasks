# collatz.py
# Author: Marcin Kaminski

""" This program asks the user to input any positive integer and outputs the successive 
values of the following calculation:

- at each step calculate the next value by taking the current value and,
if it is even, divide it by two,
but if it is odd, multiply it by three and add one.

This program ends when the current value is one. """

number = int(input("Please enter a positive integer: ")) 
# This code snippet reads in the user-suppplied
# number and converts it into an integer. 

while number != 1: # The while loop will run as long as the value of the positive integer is not equal to 1.

    print(number, end=" ")
    # This code snippet prints the number and the argument "end=" adds a space after the printed value 
    #instead of going to a new line."

    if number % 2 == 0: # If the number is even,
        number = number // 2 # then the number is divided by 2 (integer division i.e. without a remainder).
    else:               # If he number is odd,
        number = number * 3 + 1 # then the number is multiplied by 3 and then 1 is aded to the result.

print(number) # Finally, when the number becomes 1, it will be printed.

