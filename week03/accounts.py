# accounts.py
# Author: Marcin Kaminski
""" This program reads in a 10 character account number and outputs the account number
with only the last 4 digits showing (and the first 6 digits replaced with Xs). """

# The program prompts the user for an account number.
accountNumber = input("Please enter an 10 digit account number: ")
# Referenced from [2]: https://realpython.com/python-keyboard-input/

print("XXXXXX" + accountNumber[-4:])
"""This line of code creates a masked account number.
It starts with the string 'XXXXXX', and then adds the last 4 digits of the entered account 
number to that string. 
This technique is called string slicing, and it works by selecting a specific portion of text. 
In this case, '[–4:]' means 'take the last 4 characters'."""
# Referenced from [5]: https://www.geeksforgeeks.org/string-slicing-in-python/

# End


