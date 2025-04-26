# accounts-extra.py
# Author: Marcin Kaminski
""" This program reads in an account number of any length and outputs the account number
with only the last 4 digits showing. """

# The program prompts the user for an account number.
accountNumber = input("Please enter the account number: ")
# Referenced from [2]: https://realpython.com/python-keyboard-input/

num_of_x = len(accountNumber)-4 
"""This line of code calculates the number of X's needed to mask
the account number.
The 'len()' function returns the length (number of elements) of the given string or list. 
We take the length of the account number and subtract 4 from it to get the number of 'X' symbols 
needed."""
# Referenced from [4]: https://www.w3schools.com/python/ref_func_len.asp

maskedNumber = "X" * num_of_x + accountNumber[-4:]
"""This line of code creates a masked account number.
The '*' operator is used to repeat the string a specified number of times, 
in this case 'X' is repeated 'num_of_x' times. 
We then use string slicing to get the last 4 digits of the account number 
using 'accountNumber[-4:]'. 
The end result is a string composed of 'num_of_x' followed by 'X' and 
the last 4 digits of the original account number."""
# Referenced from [5]: https://www.geeksforgeeks.org/string-slicing-in-python/


print(maskedNumber)  # This line displays a masked account number

# End
