# ex33: while loops

i = 0
numbers = []

def while_loop (i, x, j):
    while i < x:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + j
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

# while_loop(i, 10, 2)

def for_loop (i, x, j):
    for i in range(i, x, j):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % (i + 1)
    print "The numbers: "

    for num in numbers:
        print num

for_loop (i, 10, 2)
