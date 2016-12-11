# Dictionaries

# create a mapping of state to abbreviation
states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}


# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print 'OR State has: ', cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

 # Do it by using the state then cities Dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

 # print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas"

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

# Map states in Australia
aust_states = {
    'New South Wales': 'NSW',
    'South Australia': 'SA',
    'Victoria': 'VIC',
    'Tasmania': 'TAS'
}

aust_cities = {
    'NSW': 'Sydney'
    'SA': 'Adelaide'
    'VIC': 'Melbourne'
}

aust_states['Western Australia'] = 'WA'
aust_states['Queensland'] = 'QLD'

print aust_states
print aust_cities

# other things you can do with Dictionaries
# del dict['Name']; # remove entry with key 'Name'
# dict.clear();     # remove all entries in dict
# del dict ;        # delete entire dictionary

#
'''
Dictionary functions:
cmp(dict1, dict2) Compares elements of both dict.

len(dict) Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.

str(dict) Produces a printable string representation of a dictionary

type(variable) Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.

Dictionary methods:
dict.clear() Removes all elements of dictionary dict

dict.copy() Returns a shallow copy of dictionary dict

dict.fromkeys() Create a new dictionary with keys from seq and values set to value.

dict.get(key, default=None) For key key, returns value or default if key not in dictionary

dict.has_key(key) Returns true if key in dictionary dict, false otherwise

dict.items() Returns a list of dict's (key, value) tuple pairs

dict.keys() Returns list of dictionary dict's keys

dict.setdefault(key, default=None) Similar to get(), but will set dict[key]=default if key is not already in dict

dict.update(dict2) Adds dictionary dict2's key-values pairs to dict

dict.values()Returns list of dictionary dict's values
'''
