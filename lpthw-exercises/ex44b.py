# Inheritance vs Composition: Override Explicitly

class Parent(object):
    def override(self):
        print "PARENT override()"

class Child(Parent):
    def override(self):
        print "CHILD override()" #overrides parent functionality

dad = Parent()
son = Child()

dad.override()
son.override()
