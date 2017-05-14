'''

Function for Typewriter-effect

'''

'''
 
Typewriter-effect for text.
 
Credits to Inbar Rose - http://stackoverflow.com/a/19911390/7620371
 
'''

import sys
from time import sleep

# We can use write() instead of print()
def write(string):              # Converted into function to re-use the code.
     
    for line in string:         # for each string
        for c in line:          # for each character in each string
            print(c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.0001)        # wait a little to make the effect look good.
    return ""                   # We want to return nothing. 
             
# http://stackoverflow.com/a/19911390/7620371
#######################################################################



# Entry point to the program
if __name__ == "__main__":
                ''

# If module was imported into another module
else:
    ''
