# ex09: printing, printing, printing


days = "Mon Tue Wed Thu Fri Sat Sun"
# \n starts a new line when printed it won't work when you use %r.
# %r is used for raw formatting used in debugging so doesn't make it pretty
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

# prints multiple lines
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
