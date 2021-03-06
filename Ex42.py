# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## is-a
class Dog(Animal):

	def __init__(self, name):
		## has-a
		self.name = name

## is-a
class Cat(Animal):

	def __init__(self, name):
		## has-a
		self.name = name

## is-a

class Person(object):
	def __init__(self, name):
	## has-a 
		self.name = name

	## Person has-a pet of some kind
		self.pet = None

## is-a
class Employee(Person):
	def __init__(self, name, salary):
	## has-a					
		super(Employee, self).__init__(name)
	## is-a
		self.salary = salary

## is-a
class Fish(object):
	pass
## is-a
class Salmon(Fish):
	pass
## is-a
class Halibut(Fish):
	pass
## rover is- a Dog
rover = Dog("Rover")
## is-a
satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan
## is-a
frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()


crouse = Salmon()

harry = Halibut()