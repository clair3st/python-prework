# Unit 3: PygLatin - part 10 - program to translate a word into pygLatin

pyg = 'ay'

original = raw_input('Enter a word: ')

word = original.lower() # lowercase version of input

first = word[0] # store first letter of the word

new_word = word[1:len(word)]+first+pyg # word is translated into PygLatin

if len(original) > 0 and original.isalpha():
    print new_word

else:
    print 'empty'
