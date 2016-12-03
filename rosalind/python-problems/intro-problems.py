def square_hyp(a, b):
    '''returns the sum of the squares of a and b'''
    return a**2 + b**2

def string_slicer(s, a, b, c, d):
    '''slice of this string (s) from indices a through b and c through d
    (with space in between), inclusively.'''
    print s[a:b+1], s[c:d+1]

def odd_sum(a, b):
    '''sum of all odd integers in between a and b'''
    total = 0
    for i in range(a, b+1):
        if i%2 != 0:
            total += i
    return total