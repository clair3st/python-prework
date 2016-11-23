# Ex 36: designing and debugging:



def start():
    print "You spend Sunday morning at a flea market."
    print "In one of the stalls you find a beautiful gold ring and a lamp."
    print "You want both, but you only have money for one. Which do you choose."

    shopping = raw_input("> ")

    if shopping == "gold ring" or shopping == "ring":
        print "You decided to buy the %s" % shopping
        gold_ring()
    elif shopping == "lamp":
        print "You decided to buy the %s" % shopping

    else:
        print "That wasn't in the shop."

def gold_ring():
    print "You put the ring on and it turns you invisible"
    print "What do you do with this power? Naughty or nice"

    ring_on = True

    ring_intent = raw_input("> ")

    while True:
        if ring_on == True and ring_intent == "nice":
            print "You can't be nice with the ring on. Take it off"
            ring_on = False
        elif ring_on == True and ring_intent == "naughty":
            print "The Lord Sauron doesn't lend his ring out to just anyone."
            bad_end()
        elif ring_on == False and ring_intent == "nice":
            print "You set out on a journey to Mount Doom"
        elif ring_on == False and ring_intent == "naughty":
            print "You need to put the ring on to achieve this"
            print "You put the ring on"
            ring_on = True

def good_end():
    print "You lived happily ever after"

def bad_end():
    print "This choose your own adventure didn't work out for you"

start()
