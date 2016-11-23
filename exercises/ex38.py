# ex38: Doing things to lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') # split ten_things with ' ' split(ten_things, ' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    #pop(more_stuff) call pop with more stuff
    print "Adding: ", next_one
    stuff.append(next_one) # append next_one to stuff
    #append(stuff, next_one) call append with stuff and next_one
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff) # Join stuff with ' ' between
# join(' ', stuff) call join with ' ' and stuff
print '#'.join(stuff[3:5]) # Join stuff[3:5] with '#' between
#join('#', stuff[3:5]) call Join with '#' and stuff[3:5]

# dir(str) lists all the attributes available to strings
