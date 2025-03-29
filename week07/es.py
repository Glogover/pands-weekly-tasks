# es.py
# Author: Marcin Kaminski
# This program reads in a text file and outputs the number of e's it contains.


# This part of the code imports two modules: 'sys' and 'os'.
import sys
import os



# This line defines a function called "count_es_in_file" which takes one argument ("FILENAME").
def count_es_in_file(FILENAME):

    try:
        with open(FILENAME, 'r') as f: # the file is opened in read mode with the name given as the function argument.
            contents = f.read()
    except FileNotFoundError: # If Python encounters a "FileNotFoundError" error while trying to open a file, an error message is displayed.
        print(f"Error: The file '{FILENAME}' does not exist.")
        return
    
    except UnicodeDecodeError: # If Python encounters a "UnicodeDecodeError" error (which usually means the file is not a text file), an error message is displayed and the function exits.
        print(f"Error: The file '{FILENAME}' may not be a text file.")
        return
    
    except IsADirectoryError: # Similarly, if Python encounters an "IsADirectoryError" error (the name supplied belongs to a directory, not a file), an error message is displayed.
        print(f"Error: '{FILENAME}' is a directory, not a text file.")
        return
    

    # This code counts the number of 'e' letters (both lowercase and uppercase).
    count = contents.count('e') + contents.count('E')

    # This is the message that will be displayed on the screen.
    print(f"The file '{FILENAME}' contains {count} e's (either lowercase or uppercase).")

# Fetching file name from command line arguments.
    
# This is the standard way in Python to determine whether a script is being run directly (rather than imported as a module).
if __name__ == "__main__":

# Here the code checks if the user has provided a filename as an argument on the command line. If not, an error message is displayed.
    if len(sys.argv) < 2:
        print("Error: Please provide the filename as a command line argument.")
    else:

# If the user provided a file name as an argument on the command line, the file name is assigned to the variable 'filename' and then the function 'count_es_in_file' is called with that name.
        FILENAME = sys.argv[1]
        count_es_in_file(FILENAME)