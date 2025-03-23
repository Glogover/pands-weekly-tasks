# squareroot.py
# Author: Marcin Kaminski

""" This program takes a positive floating-point number as input and outputs an 
approximation of its square root.
"""

def sqrt(n):
    """
    Function to calculate square root of a number using Newton's method
    """

    """
    We initialize the variable "approx" as our first estimate of the sqaure root,
    starting with the value of n divided by 2
    """
    
    approx = float(n)/2.0

    """
    We then calculate a better estimate "better_approx", using Newton's method. 
    This is the average of approx and n/approx.
    """

    better_approx = (approx + float(n)/approx)/2.0

    """
    We start a while loop that will continue until our better approximation is equal to 
    our current approximation. 
    This means we will keep updating our approximation as long as we are able to improve it.
    """

    while better_approx != approx:
        approx = better_approx
        better_approx = (approx + float(n)/approx)/2.0

    """Once we're done improving our estimate, we return it as the result. 
    This is our estimated value of the square root of n."""

    return approx


#print(sqrt(25))  # For testing, we know square root of 25 is 5. It should return 5.

n  = input("Please enter a positive number: ")
print(f"The square root of {n} is approx. {sqrt(n)}")