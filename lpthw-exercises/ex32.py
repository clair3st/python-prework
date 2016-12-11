# ex32: loops and lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricts']
change = [ 1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

# can go through mixed lists too. have to use %r since we don't know what's in it.
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# use range function to do 0 to 5 counts
# range return a list of integers, not inclusive
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function lists understands
    elements.append(i)

 # now we can print them out too
for i in elements:
    print "Element was: %d" % i
