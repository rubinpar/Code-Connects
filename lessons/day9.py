class School:
    def __init__(self):
        self.students = 0

    def factory(type):
        if type =="Elementary":
            return Elementary()
        if type =="Middleschool":
            return Middleschool()
        if type =="Highschool":
            return Highschool()
        assert 0, "Bad School creation:" + type

    def addStudents (self, num):
        self.students += num

class Elementary(School):
    def lunchBreak (self):
        print ("30 min lunch and 30 min recess")

class Middleschool (School):
    def lunchBreak (self):
        print ("45 min lunch")

class Highschool(School):
    def lunchBreak(self):
        print("3 hour lunch")

school = School()
print(school.students)
school.addStudents(70)
print(school.students)

my_highschool = Highschool()
my_highschool2 = School.factory("Highschool")

# Suppose we are writing code to track different types of cars in a race. There
# are three types of cars, a sports car, a van, and a truck. For one move, a
# sports car moves 5 miles forward, a van 3, and a truck 1. Each move uses
# one gallon of gas; and a sports car starts with 10 gallons, and van with 15 and
# a truck with 25. Write some code using factory methods that tracks the gas
# and units travelled of each vehicle.


class Vehicle:
    def __init__(self, speed=0, tank=0):
        self.location = 0
        self.tank = tank
        self.gas = tank
        self.speed = speed

    def factory(kind):
        if kind == "Van":
            return Van

    def add_location(self, num):
        self.location += num

    def subtract_gas(self, num):
        self.gas -= num

    def move(self):
        self.add_location(self.speed)
        self.subtract_gas(1)

class Van(Vehicle):
    def __init__(self):
        super().__init__(speed=3, tank=15)

# v = Vehicle(tank=1000, speed=50)
# v2 = Vehicle(1000, 50)
# print(v.speed, v.tank)
# print(v2.speed, v2.tank)
scooby_van = Vehicle.factory("Van")

my_van = Van()
# my gas to be 15, location to be 0
print(my_van.gas, my_van.location)
my_van.move()
# my gas to be 14, location to be 3
print(my_van.gas, my_van.location)
my_van.move()
# my gas to be 13, location to be 6
print(my_van.gas, my_van.location)
