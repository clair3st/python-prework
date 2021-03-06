# Ex42: Is-a, Has-a, Objects and Classes

# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    """docstring for Animal"""
    pass

# Dog is-a Animal
class Dog(Animal):
    """docstring for Dog"""
    def __init__(self, name):
        # dog has a name
        self.name = name

# Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        # cat has-a name
        self.name = name

        def say_name():
            print 'my name is ', name

# Person is-a object
class Person(object):
    def __init__(self, name):
        # person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        #  ? hmm what is this strange magic? employee has-a name
        super(Employee, self).__init__(name)
        # employee has-a salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

# Salmon is-a fish
class Salmon(Fish):
    pass

# Halibut is-a Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# Satan is a Cat
satan = Cat("Satan")

# Mary is a person
mary = Person("Mary")

# Mary has a pet Satan
mary.pet = satan

# frank is a Employee
frank = Employee("Frank", 120000)

# frank has a pet rover
frank.pet = rover

# flipper is a fish
flipper = Fish()

# crouse is a salmon
crouse = Salmon()

# harry is a halibuy
harry = Halibut()
