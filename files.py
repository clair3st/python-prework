def read_even(filename):
    i = 1
    for line in open(filename):
        if i % 2 == 0:
            print line,
        i+=1
