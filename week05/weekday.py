# weekday.py
# Author: Marcin Kaminski
# This program outputs whether or not today is a weekday. 

import datetime # Importing datetime module
# Referenced from [11]: https://docs.python.org/3.12/library/datetime.html

current_date= datetime.datetime.today()  # Getting current date
# Referenced from [12]: https://www.w3schools.com/python/python_datetime.asp

day_of_the_week_integer = current_date.weekday() # Getting weekday number
# Referenced from [12]: https://www.w3schools.com/python/python_datetime.asp

""" 
weekday() function returns the integer mapping corresponding to the specified day
of the week.
Below listing shows the integer values corresponding to the day of the week.

0 Monday
1 Tuesday
2 Wednesday
3 Thursday
4 Friday
5 Saturday
6 Sunday

"""

# Checking if today is the weekend
if day_of_the_week_integer == 5 or day_of_the_week_integer == 6:
    print("It is the weekend, yay!")
else: # Monday to Friday are considered a weekday
    print("Yes, unfortunately today is a weekday.")
# Referenced from [13]: https://realpython.com/python-conditional-statements/

# End