""" Copyright (c) 2017 Capital One

 This software
 Capital One
 any form or medium,
 any manner"""

"""Author: Ali Bhagat
This script helps to build"""

import time

print('Press Enter')
while True:
    try:
        input() # FOR ENTER, ...
        starttime = time.time()
        print("Started")
    except KeyboardInterrupt:
        print("Stopped")
        endtime = time.time()
        print('Total Time:', round(endtime - starttime, 2), 'secs')
        break

# Define again() function to ask user if they want to use the calculator again
def again():

    # Take input from user
    calc_again = input('''
                        Do you want to calculate again?
                        Please type Y for YES or N for NO.
                        ''')

    # If user types Y, run the calculate() function
    if calc_again == 'Y':
        calculate() # Inline comment about the code

    # If user types N, say good-bye to the user and end the program
    elif calc_again == 'N':
        print('See you later.')

    # If user types another key, run the functiona again
else:
    again()


def calculate():
    # TODO: Implement the calculate function

def input():
    # TODO: Implement this function
    return 'Dummy'

def realpath(path):
    """
    Returns the true, canonical file system path equivalent to the given path.
    """
    """ TODO: There may be a more clever way to do this that also handles other,
     less common file systems."""
    return os.path.normpath(normcase(os.path.realpath(path)))

