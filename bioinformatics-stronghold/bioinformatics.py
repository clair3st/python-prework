def counting_DNA(s):
    '''Four integers (separated by spaces) counting the respective number
    of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.'''
    print s.count('A'), s.count('C'), s.count('G'), s.count('T')

def transcribe_DNA(t):
    '''return the transcribed RNA string for an input DNA string t'''
    print t.replace('T', 'U')

def reverse_complement(t):
    '''return the reverse complement of a DNA string'''
    base_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    bases = [base_pairs[x] for x in t]
    t = ''.join(bases)
    return t[::-1]

def fibs_rabbits(n, k):
    '''return the number of breeding pairs after n months
    with k brood size'''
    if n is 0 or n is 1:
        return 1
    else:
        return (fibs_rabbits(n-1, k) + k * fibs_rabbits(n-2, k))
