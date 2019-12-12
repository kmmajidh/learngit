## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## dog is a animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has a name
        self.name = name

## cat is an animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has a name
        self.name = name

## Person is an object
class Person(object):

    def __init__(self, name):
        ## Person has a name
        self.name = name

        ## Person has a pet
        self.pet = None

##Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has name and pet. hmm what is this strange magic?"
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

## Fish is an object
class Fish(object):
    pass

## salmon is a fish
class Salmon(Fish):
    pass

## Halibut is a fish
class Halibut(Fish):
    pass


## rover is a dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## Mary has satan
mary.pet = satan

#frank is an employee
frank = Employee("Frank", 120000)

## Frank has rover
frank.pet = rover

##Flipper is fish
flipper = Fish()

## Crouse is a salmon
crouse = Salmon()

## Harry is a halibut
harry = Halibut()
