# ex21: Functions can return something

# python adds the two numbers, when anyline that runs the function
# can assign the result to a variable. can be anything put to the right of =
def add(a, b):
    print "ADDIN %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for extra credit:
print "Here's a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# 35 + (74 - (180 * (50 / 2)))

print "That becomes: ", what, "Can you do it by hand?"
