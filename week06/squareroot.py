# squareroot.py
# Author: Marcin Kaminski

""" This program takes a positive floating-point number as input and outputs an 
approximation of its square root.
"""

def sqrt(n):
    """
    Function to calculate square root of a number using Newton's method.
    """
    # Refrenced from [14]: https://en.wikipedia.org/wiki/Newton%27s_method

    # This function takes a positive number n as input and returns its square root.
    # The function uses Newton's method to iteratively improve the approximation of the square root.
    # The method starts with an initial guess (approx) and refines it using the formula below.
    # The process continues until the approximation converges to a stable value.
        
    """
    We initialize the variable "approx" as our first estimate of the square root,
    starting with the value of n divided by 2.0.
    """
    
    approx = float(n)/2.0 # "float(n)"" used to replace string "n" with floating-point number "n"

    """
    We then calculate a better estimate "better_approx", using Newton's method. 
    This is the average of approx and n/approx. 
    """
    # Referenced from [15]: https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf

    # The formula for Newton's method is:
    better_approx = (approx + float(n)/approx)/2.0

    """
    We start a while loop that will continue until our better approximation is equal to 
    our current approximation. 
    This means we will keep updating our approximation as long as we are able to improve it.
    """
    
    while better_approx != approx:
        approx = better_approx
        better_approx = (approx + float(n)/approx)/2.0
    # Referenced from [16]: https://www.w3schools.com/python/python_while_loops.asp
        

    """Once we're done improving our estimate, we return it as the result. 
    This is our estimated value of the square root of n.
    """

    return approx
    # Referenced from [17]: https://www.w3schools.com/python/python_functions.asp


#print(sqrt(25))  # For testing, we know square root of 25 is 5. It should return 5.

n  = input("Please enter a positive number: ") # This code snippet reads in the user-supplied 
# number and converts it into a floating-point number.

print(f"The square root of {n} is approx. {sqrt(n)}") # This code snippet prints the result of 
#the function "sqrt" with the user-supplied number as an argument.


# End