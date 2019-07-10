# Make a pet store!
# Want animal objects... what are their states, their operations?
# We also want a pet store that has a selection of animals for customers
# to choose from. So what's its state? And what might a pet store have to do
# as operations, e.g. get more pets, feed a pet

class Animal:
    def __init__(self, weight, height, age):
        """
        weight in pounds
        height in inches
        age in years
        """
        self.weight = weight
        self.height = height
        self.age = age

    def gain_weight(self, change):
        self.weight += change

    def __str__(self):
        return "This animal weighs {} pounds.".format(self.weight)

class Pet(Animal):
    def __init__(self, owner, name, weight, height, age):
        Animal.__init__(self, weight, height, age)
        self.owner = owner
        self.name = name

    def __str__(self):
        return "{} is owned by {}.".format(self.name, self.owner)

class Dog(Pet):
    def __init__(self, owner, name, weight, height, age):
        Pet.__init__(self, owner, name, weight, height, age)

    def bark():
        print("BARK BARK!")

# animal1 = Animal(110, 48, 7)
# print(animal1)
# kosmo = Dog("Marko", "Kosmo", 45, 28, 7)
# print(kosmo)
# print(kosmo.weight)
# kosmo.gain_weight(40)
# print(kosmo.weight)
# kosmo.bark()

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Employee(Person):
    def __init__(self, name, position, rate, address):
        Person.__init__(self, name)
        self.position = position
        self.rate = rate
        self.address = address

        self.hours_worked = 0

    def receive_paycheck(self):
        amount = self.rate * self.hours_worked
        print("{}'s check for {} sent to {}.".format(self.name,
                                                    amount, self.address))
        self.hours_worked = 0

    def log_hours(self, hours):
        self.hours_worked += hours

    def __str__(self):
        return "{} gets paid {} per hour".format(self.name, self.rate)

marcus = Employee("Marcus", "Cashier", 15, "880 36th Street")
marcus.log_hours(43)
marcus.log_hours(50) #93
marcus.receive_paycheck()
marcus.log_hours(33)
marcus.log_hours(50)
marcus.log_hours(10) #93
marcus.receive_paycheck()

class Manager(Employee):
    def __init__(self, name, rate, address, employees):
        Employee.__init__(self, name, "Manager", rate, address)
        self.employees = employees

    def hire_employee(self, employee):
        self.employees.append(employee)

    def fire_employee(self, employee):
        employee.receive_paycheck()
        employee.rate = 0
        self.employees.remove(employee)

class SeasonalEmployee(Employee):
    def __init__(self, name, position, rate, address, end_date):
        Employee.__init__(self, name, position, rate, address)
        self.end_date = end_date


rubin = Manager("Rubin", 30, "NYC", [marcus])
rubin.log_hours(60)
rubin.log_hours(20)
rubin.receive_paycheck()
marcus.log_hours(12)
print(rubin.employees)
rubin.fire_employee(marcus)
print(rubin.employees)
jimbob = Employee("Jim Bob", "Cashier", 15, "Colorado")
lucy = Employee("Lucy", "Cashier", 15, "California")
rubin.hire_employee(jimbob)
rubin.hire_employee(lucy)
print(jimbob.address)
print(lucy.address)


class Customer(Person):
    pass

# Make an animation thing a ma bob
# Character class: position,  outfit, move around, walk
    # --- princess, dragon
# Scene: a set of actions of actions and characters
# Set:
# Scenery: subclasses, Trees, Stones,
