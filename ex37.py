# Ex37: Symbol review

# and - logic expression to look for more than one Boolean
print "and"
if 2 == 2 and 1 == 1:
    print "2 == 2 AND 1 == 1"

# del - delete variable or item.
list_item = ['bird', 'cat', 'horse']
print "del"
print "list is %s" % list_item
del list_item[1]
print "list is %s" % list_item

# from - from keyword from import statement. used to define a name in the local
#  namespace for a given module
print "from and import"
print "from sys import exit"

# not - keyword for boolean expression opposite of statement evaluated
print "not"
if not 2 == 3:
    print "not 2 == 3"

# while - loop for as long as an expression is True
print "While"
x = 0
while x < 2:
    print x
    x += 1

# as - asign output of a with statement to a new variable
# It's handy when you have two related operations which you want to execute as a pair,
# with a block of code in between.
# print 'with and as'
# with open(new_file.txt, 'r') as f:
#     read_data = f.read()
#     f.closed

# elif - else if, after first if statement subsequent if
# if - executes block of code if satement is True
print "elif and if"
if 2 == 3:
    print "is two equal to 3"
elif 2 == 2:
    print "2 is 2"

# global - namespace outside of functions etc
x = 0
print 'x is a global variable which is %d' % x

# or - Boolean comparision needs either to be true
print "or"
if 2 == 2 or 1 == 2:
    print "2 == 2 or 1 == 2, one of these is true"

# else - runs if no other if statements before executes. good way to make sure
# something executes
print "else"
if 2 == 3:
    print "is two equal to 3"
else:
    print "This prints because everything else is False"

# pass - none statement, means nothing gets executed. used as a placehoder
def fname(arg):
    pass #this means the function won't fun until removed

# yield - part of generator function in which a series of values can be returned
# when yeild is called the function is 'frozen'
print "yield"
def simple_generator_function():
    yield 1
    yield 2
    yield 3
print"execute"
for value in simple_generator_function():
    print(value)
print "use next()"
our_generator = simple_generator_function()
next(our_generator)
next(our_generator)
next(our_generator)

# break - terminates a for or while loop
print "break"
x = 0
while x < 2:
    if x == 1:
        break
    print x
    x += 1

# except - in a try statement, used to handle exceptions such as nameErrors
print "except and try"
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again")

# print - outputs string. converts to string if need be
print "this is a print"

# class
print "class"
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

# exec - executing a dynamically created statement or program


# in - used to iterate over a sequence applying a comparision
print 'in'
for x in list_item:
    print x

# raise - forces a specified exception to occur
print "raise"
# raise NameError('HiThere')

# continue - breaks a loop and continues after a condition
# print "continue"
# x = 0
# while x < 2:
#     if x == 1:
#         continue
#     print x
#     x += 1

# finally - in a try statement, always executed before end
# print 'finally'
# try:
#     raise KeyboardInterrupt
# finally:
#     print 'Goodbye, world!'

# is - For comparing against None, is None is preferred over == None
print 'is'
print '[] is not []'
[] is not []

# return - returns values out of a function

# def - definition of a function
print "def"
def f (x): return x ** 2
print f(8)

# for - used to iterate over a sequence
print "for"
for x in range(0,4):
    print x


# lambda - anonymous function call
print "lambda"
g = lambda x: x ** 2
print g(8)


print '''Data types'''
# Boolean
True
False
# None
None
# string
'string'
# numbers
1, 2
# floats
1.4
# lists
['list', 3, 1.2, True, None]


print 'String Escape Sequence'

print '\\ Backslash'
print '\' single quote'
print '\" quote'
print '\a bell'
print 'backk\bspace '
print 'form\ffeed'
print 'line\nfeed'
print 'carriage\rreturn'
print '\ttab'
print 'vertical\vtab'

print 'String Formats'

print 'signed integer decimal: %d' % 5
print 'signed integer decimal: %i' % 5
print 'signed octal value: %o' % 5
print 'signed integer decimal: %u' % 5
print 'signed hexadecimal (lowercase): %x' % 5
print 'signed hexadecimal (uppercase): %X' % 5
print 'Floating point exponential format (lowercase): %e' % 2.5
print 'Floating point exponential format (uppercase): %E' % 2.6
print 'Floating point exponential format (lowercase): %f' % 2.6
print 'Floating point exponential format (uppercase): %F' % 2.6
print 'Floating point format: %g' % 2.65
print 'Floating point format: %G' % 2.65
print 'Single character: %c' % 'c'
print 'String: %r' % 8
print 'String: %s' % 4
print 'no conversion %%' 


print 'Operators'

2 + 3
5 - 3
2 * 1
2 ** 2
6 / 2
6 // 2
6 % 2
6 < 2
6 > 2
4 <= 5
4 >= 6
4 == 5
4 != 5
4 <> 5 # If values of two operands are not equal, then condition becomes true.
# ()
# []
# {}
# @
# '
# :
# .
# =
# ;
# +=
# -=
# *=
# /=
# //=
# %=
# **=
