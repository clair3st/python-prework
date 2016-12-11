# ex19: functions and Variables

# function definition, the function has two arguments which get printed on
# the following lines
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# envokes function with 20 and 30 as the arugments
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# defines variables for cheese and crackers then calls function with these
# arguments
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# envoke function with math
print "We can even do math inside too:"
cheese_and_crackers(10 +20, 5 + 6)

print "ANd we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
