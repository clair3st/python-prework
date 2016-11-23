# Inheritance vs Composition: Implicit Inheritance

class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass #nothing new to create

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
