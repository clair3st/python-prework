# ex10: What was That?

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# triple single quotes will do the same thing
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# while True:
#     for i in ["/", "-", "|", "\\", "|"]:
#         print "%s\r" % i,

# %r will print out the raw representation of what you types
# which includes the original excape sequences. Use %s

# %r is for debugging and % is for displayin

# Study goals

example = "what does \f do?"

print example
