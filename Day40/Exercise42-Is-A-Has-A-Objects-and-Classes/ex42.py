## Animal is-a object(yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a object
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name
## Cat is-a object
class Cat(Animal):

    def __int__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a  name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a kind of Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## person has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a object
class Salmon(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## saten is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet is-a Cat named saten
mary.pet = satan

## frank is-a Employee and has-a salary about 1200000 
frank = Employee("Frank", 1200000)

## frank has-a pet is-a Dog named rover
frank.pet = rover

## fish has-a flipper
flipper = Fish()

## salmon has-a crouse
crouse = Salmon()

## harry is-a halibut
harry = Halibut()
