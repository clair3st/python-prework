# TODO: Define a function is_even that will take a number x as input.
# If x is even, then return True.
# Otherwise, return False.
def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False

# TODO: Define a function is_int that takes a number x as an input.
# Have it return True if the number is an integer (as defined above) and False otherwise.
def is_int(x):
    if x%1 == 0: return True
    else: return False

# TODO: Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits.
# For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.
def digit_sum(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total

# TODO: Define a function factorial that takes an integer x as input.
# Calculate and return the factorial of that number.
def factorial(n):
    total = 1
    for i in range(n, 0, -1):
        total *= i
    return total

# TODO: Define a function called is_prime that takes a number x as input.
# For each number n from 2 to x - 1, test if x is evenly divisible by n.
# If it is, return False.
# If none of them are, then return True.
def is_prime(x):
    answer = False
    if x < 2: answer = False
    elif x == 2 or x == 3: answer = True
    else:
        for n in range(2, x - 1):
            if x % n == 0:
                answer =  False
                break
            else:
                answer = True
    return answer

# TODO: Define a function called reverse that takes a string textand returns that string in reverse.
#
# For example: reverse("abcd") should return "dcba".
#
# You may not use reversed or [::-1] to help you with this.
# You may get a string containing special characters (for example, !, @, or #).
def reverse(text):
    output = ''
    count = len(text)-1
    while count >= 0:
        output += text[count]
        count -= 1
    return output

# TODO: Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.
#
# For example: anti_vowel("Hey You!") should return "Hy Y!".
#
# Don't count Y as a vowel.
# Make sure to remove lowercase and uppercase vowels.
def anti_vowel(text):
    vowels = 'aeiouAEIOU'
    no_vowels = ''
    for char in text:
        if char in vowels:
            continue
        else:
            no_vowels += char
    return no_vowels

# TODO: Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word.
#
# Assume your input is only one word containing no spaces or punctuation.
# As mentioned, no need to worry about score multipliers!
# Your function should work even if the letters you get are uppercase, lowercase, or a mix.
# Assume that you're only given non-empty strings.
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
    word_score = 0
    for char in word.lower():
        for letter in score:
           if letter == char:
               word_score += score[letter]
    return word_score

# TODO: Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.
#
# For example:
#
# censor("this hack is wack hack", "hack")
# should return
#
# "this **** is wack ****"
# Assume your input strings won't contain punctuation or upper case letters.
# The number of asterisks you put should correspond to the number of letters in the censored word.

def censor(text, word):
    list_text = text.split(' ')
    answer = ''
    for i in list_text:
        if i == word:
            i = '*'*len(word)
            answer += (i + ' ')
        else: answer += (i + ' ')
    answer = answer[:-1]
    return answer

# TODO: Define a function called count that has two arguments called sequence and item.
# Return the number of times the item occurs in the list.
# For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).
#
# There is a list method in Python that you can use for this, but you should do it the long way for practice.
# Your function should return an integer.
# The item you input may be an integer, string, float, or even another list!
# Be careful not to use list as a variable name in your code—it's a reserved word in Python!

def count(sequence, item):
    answer = 0
    for i in sequence:
        if i == item: answer += 1
    return answer


# TODO: Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result.
def purify(number_list):
    answer = []
    for i in number_list:
        if i%2 == 0: answer.append(i)
    return answer


#TODO: Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list.
def product (number_list):
    answer = 1
    for i in number_list:
        answer *= i
    return answer

# TODO: Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.
def remove_duplicates(list_eg):
    answer = []
    for i in list_eg:
        if i in answer:
            continue
        else:
            answer.append(i)
    return answer

#TODO: Write a function called median that takes a list as an input and returns the median value of the list.
def median(input_list):
    input_list = sorted(input_list)
    length = len(input_list)
    if length%2 == 0:
        answer = (input_list[length/2] + input_list[(length-1)/2]) / 2.0
    else:
        answer = input_list[length//2]
    return answer
