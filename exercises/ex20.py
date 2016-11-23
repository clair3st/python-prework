# Ex20: FUnctions and Files

# import adds modules to script from the python module set.
# keeps programs small by only adding modules you plan to use.
# argv is argument variable this holds arguments you pass to your
# Python script when run.
from sys import argv

# unpack script and filename
script, input_file = argv

# function that reads the file 'f'
def print_all(f):
    print f.read()

# function seeks a file at beginning
def rewind(f):
    print f.seek(0)

# function with argunment of line_count and f, output line_count and readline()
def print_a_line(line_count, f):
    print line_count, f.readline(),

# open file and save object in variable
current_file = open(input_file)

# print whole file using defined function
print "First let's print the whole file:\n"
print_all(current_file)

# put back to the beginning
print "Now let's rewind, kind of like a tape"
rewind(current_file)

# print line by line with function calls
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
