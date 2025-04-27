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
# Referenced from [6]: https://www.w3schools.com/python/python_user_input.asp

while number != 1: # The while loop will run as long as the value of the positive integer is not equal to 1.
# Referenced from [7]: https://www.w3schools.com/python/python_while_loops.asp
    
    print(number, end=" ")
    # This code snippet prints the number and the argument "end=" adds a space after the printed value 
    #instead of going to a new line."
    # Referenced from [8]: https://stackoverflow.com/questions/63569902/whats-the-meaning-of-print-end-in-python


    if number % 2 == 0: # If the number is even,
        number = number // 2 # then the number is divided by 2 (integer division i.e. without a remainder).
    else:               # If he number is odd,
        number = number * 3 + 1 # then the number is multiplied by 3 and then 1 is aded to the result.
    # Referenced from [9]: https://365datascience.com/question/please-explain-if-x-2-0/

print(number) # Finally, when the number becomes 1, it will be printed.


# This code is a simple implementation of the Collatz conjecture,
# which is a conjecture in mathematics that states that no matter what positive integer you start with,
# you will always eventually reach 1 by following the above rules.

# Referenced from [10]: https://en.wikipedia.org/wiki/Collatz_conjecture

# End
