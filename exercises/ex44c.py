# Inheritance vs Composition: Alter Before or after

class Parent(object):
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered() #call super and call function altered on parent
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
