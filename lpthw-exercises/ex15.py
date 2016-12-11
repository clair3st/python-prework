# ex15: Reading files

# from the sys module import argv function
from sys import argv

# argument variable to pass to python script when run, unpacked to hold
# a filename
script, filename = argv

# varibale txt is assigned to open function to open the script, returns a
# file object
txt = open(filename)

# text to show filename trying to open using the raw formatting variable
print "Here's your file %r:" % filename
# call the read function on txt variable. txt returns a file which you tell it to read
print txt.read()
txt.close()

# print string for prompt raw input from user
print "Type the filename again:"
file_again = raw_input("> ")

# opens the filename again
txt_again = open(file_again)

# prints the output of reading the filename
print txt_again.read()
txt.close()
