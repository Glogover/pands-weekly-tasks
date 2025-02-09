# bank.py
""" 
The program:
- Prompts the user and reads in two money amounts (in cent)
- Adds the two amounts
- Prints out the answer in a human readable format with a euro 
  sign and decimal point between the euro and cent of the amount 
"""

amount1 = int(input("Enter amount 1 (in cent): "))
amount2 = int(input("Enter amount 2 (in cent): "))
answer = (amount1 + amount2)/100
print(f"The sum of these is €{answer}")
      
# End