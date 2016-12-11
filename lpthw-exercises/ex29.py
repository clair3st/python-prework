 # Ex29: What IF

people = 20
cats = 30
dogs = 15

# if statement uses a conditional and executes the block of code under it if True
# needs to be indented to tell python it is in the same block, won't work otherwise


if people < cats:
     print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."
