# accounts-extra.py
""" This program reads in an account number of any length and outputs the account number
with only the last 4 digits showing. """
# Author: Marcin Kaminski

accountNumber = input("Please enter the account number: ")

num_of_x = len(accountNumber)-4 
"""This line of code calculates the number of X's needed to mask
the account number"""


maskedNumber = "X" * num_of_x + accountNumber[-4:]
"""This line of code creates a masked account number"""

print(maskedNumber)  # This line displays a masked account number


