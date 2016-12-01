def word_counter(s):
    counts = dict()
    for word in s.split(' '):
        counts[word] = counts.get(word, 0) + 1
    for key, value in counts.items():
        print key, value
