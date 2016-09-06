# Ex16: Reading and Writing files

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

# difference between 'w' mode and truncate() is that 'w' mode automatically
# wipes the entire file for us to rewrite it, and truncate() allows us to
# choose how much or little of the file's contents we want to delete depending
# on parameters (without parameters truncate works exactly the same as
# 'w' mode)

print "Opening the file..."
print filename , "file's name"
target = open(filename, 'r+')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# target.write(line1)
# target.write("/n")
# target.write(line2)
# target.write("/n")
# target.write(line3)
# target.write("/n")

target.write("%r/n%r/n%r/n" % (line1, line2, line3))

# add reading of file
print "We're going to read %r." % filename
# txt = open(filename, 'r')
print target.read()


print "And finally, we close it."
target.close()
