## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal class
class Dog(Animal):

    def __init__(self, name):
        ## __init__ is-a Dog's method
        self.name = name

## Cat is-a Animal class
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person class
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a Person __init__ method
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish class
class Salmon(Fish):
    pass

## Halibut is-a Fish class
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

##  satan is-a Cat
satan = Cat("Satan")

## mary is-s Person
mary = Person("Mary")

## mary pet is-a satan
mary.pet = satan

## frank is-a Employee, frank has-a salary 120000
frank = Employee("Frank", 120000)

## frank pet is-a rover
frank.pet = rover

## flipper is-a Fish Instance
flipper = Fish()

## crouse is-a Salmon Instance
crouse = Salmon()

## harry is-a Halibut Instance
harry = Halibut()