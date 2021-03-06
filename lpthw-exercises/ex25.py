# Ex25: Even more practice

def break_words(stuff):
    """This function will break up words for us.""" #this is a documentation comment
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """"Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(sentence)
    print_last_word(sentence)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# Output of terminal testing
#     Python 2.7.10 (default, Jul 14 2015, 19:46:27)
# [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import ex25  --this makes a module with function in it. to get access to all functions do from ex25 import *
# >>> sentence = "All good things come to those who wait."
# >>> words = ex25.break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words)
# All
# >>> ex25.print_last_word(words)
# wait.
# >>> words
# ['good', 'things', 'come', 'to', 'those', 'who']
# >>> ex25.print_first_word(sorted_words)
# All
# >>> ex25.print_last_word(sorted_words)
# who
# >>> sorted_words
# ['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last_sorted(sentence)
# All
# who
