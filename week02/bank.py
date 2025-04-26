# bank.py
# Author: Marcin Kaminski
""" 
This program:
- Prompts the user and reads in two money amounts (in cent)
- Adds the two amounts
- Prints out the answer in a human readable format with a euro 
  sign and decimal point between the euro and cent of the amount. 
"""

# The program prompts the user for two amounts in cent.
# These values ​​are stored as integers in the variables 'amount1' and 'amount2'.
amount1 = int(input("Enter amount 1 (in cent): "))
amount2 = int(input("Enter amount 2 (in cent): "))
# Referenced from [2]: https://realpython.com/python-keyboard-input/

# The amounts are in cent, so we need to divide by 100 to get euro.
# The result is stored in the variable 'answer'.
answer = (amount1 + amount2)/100

# The f-string is used to format the output.
print(f"The sum of these is €{answer}")
# Referenced from [3]: https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/


# End