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
    if n is 2:
        return k
    if n <= 4:
        return fibs_rabbits(n-1, k) + fibs_rabbits(n-2, k)
    else:
        return (fibs_rabbits(n-1, k) + (k * fibs_rabbits(n-2, k)))

def highest_GC_content(d):
    x = d.split('\n')
    percents = []
    def GC_content(s):
        return ((float(s.count('G'))+float(s.count('C')))/float(len(s)))*100
    for i in range(1, len(x), 2):
        percents.append(GC_content(x[i]))
    highest_GC = index(max(percents))
    return highest_GC #TODO: need to work out how to slit so get whole DNA strand, also need to work out how to return result
