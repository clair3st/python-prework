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

    
