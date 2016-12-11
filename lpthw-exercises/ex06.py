# Ex6: Strings and Text

# x is defined as a string influding %d format variable set to 10
x = "There are %d types of people." % 10
# binary and do_not variable is defined as a string
binary = "binary"
do_not = "don't"
# y is defined as a string containing two format variables which are predefined variables
y = "Those who know %s and those who %s." % (binary, do_not) # no.1 string in a string

# prints variables x and y
print x
print y

# prints string using format variable set to x and y (which is also a string containing format variable)
# %r is for debugging
print "I said: %r." % x  # no.2 string in a string
print "I also said: '%s'." % y  # no.3 string in a string

# hilarious is given a boolean and joke is a string with debugging format varibale
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#execute print function defining the format variable as hilarious
print joke_evaluation % hilarious  # no.4 string in a string

# defines w and e as strings
w = "This is the left side of..."
e = "a string with the right side."

# executes print of w and e and concats together.
print w + e
