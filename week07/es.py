# es.py
# Author: Marcin Kaminski
# This program reads in a text file and outputs the number of e's it contains.


# This part of the code imports two modules: 'sys' and 'os'.
import sys
# The 'sys' module provides access to some variables used or maintained by the 
# interpreter and to functions that interact with the interpreter.
# Referenced from [18]: https://docs.python.org/3.12/library/sys.html
import os
# The 'os' module provides a way of using operating system-dependent functionality 
# like reading or writing to the file system.
# Referenced from [19]: https://docs.python.org/3.12/library/os.html


# This line defines a function called "count_es_in_file" which takes one argument ("FILENAME").
def count_es_in_file(FILENAME):

    try:
        with open(FILENAME, 'r') as f: # the file is opened in read mode with the name given as the function argument.
            contents = f.read()
            # Referenced from [20]: https://www.w3schools.com/python/python_file_handling.asp
    except FileNotFoundError: # If Python encounters a "FileNotFoundError" error while trying to open a file, an error message is displayed.
        print(f"Error: The file '{FILENAME}' does not exist.")
        return
    # Referenced from [21]: https://www.w3schools.com/python/python_try_except.asp
    # Referenced from [22]: https://stackoverflow.com/questions/17658856/why-am-i-getting-a-filenotfounderror

    except UnicodeDecodeError: # If Python encounters a "UnicodeDecodeError" error (which usually means the file is not a text file), an error message is displayed and the function exits.
        print(f"Error: The file '{FILENAME}' may not be a text file.")
        return
    # Referenced from [23]: https://wiki.python.org/moin/UnicodeDecodeError

    
    except IsADirectoryError: # Similarly, if Python encounters an "IsADirectoryError" error (the name supplied belongs to a directory, not a file), an error message is displayed.
        print(f"Error: '{FILENAME}' is a directory, not a text file.")
        return
    # Referenced from [24]: https://docs.python.org/3.12/library/exceptions.html#IsADirectoryError
    

    # This code counts the number of 'e' letters (both lowercase and uppercase).
    count = contents.count('e') + contents.count('E')
    # Referenced from [25]: https://www.w3schools.com/python/python_strings_methods.asp

    # This is the message that will be displayed on the screen.
    print(f"The file '{FILENAME}' contains {count} e's (either lowercase or uppercase).")

# Fetching file name from command line arguments.    
# This is the standard way in Python to determine whether a script is being run directly (rather than imported as a module).
if __name__ == "__main__":
# Referenced from [26]: https://realpython.com/if-name-main-python/

# Here the code checks if the user has provided a filename as an argument on the command line. If not, an error message is displayed.
    if len(sys.argv) < 2:
        print("Error: Please provide the filename as a command line argument.")
    else:
    # The 'sys.argv' list contains the command line arguments passed to the script.
    # The first element, 'sys.argv[0]', is the name of the script itself.
    # The second element, 'sys.argv[1]', is the first argument passed to the script.
    # In this case, the script expects a filename as the first argument.
    # Referenced from [27]: https://docs.python.org/3.12/library/sys.html#sys.argv
        

# If the user provided a file name as an argument on the command line, the file name is assigned to the variable 'filename' and then the function 'count_es_in_file' is called with that name.
        FILENAME = sys.argv[1]
        count_es_in_file(FILENAME)

# End
        
        