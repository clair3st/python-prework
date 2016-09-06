# Ex13: Parameters, Unpacking, Variables

# import adds modules to script from the python module set.
# keeps programs small by only adding modules you plan to use.
# argv is argument variable this holds arguments you pass to your
# Python script when run.
from sys import argv

# unpacks argv, argv gets assigned to 4 variables that can be manipulated
script, first, second, third = argv

second = raw_input("what is your favorite color? ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Sys module: This module provides access to some variables used or maintained
# by the interpreter and to functions that interact strongly with the interpreter.
#  It is always available.

# sys.argv
# The list of command line arguments passed to a Python script. argv[0] is the
 # script name (it is operating system dependent
 # whether this is a full pathname or not).

 # get a value error if too many or too little variables are passed to the script
