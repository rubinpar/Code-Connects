class Complex:
    """
    Represents a complex number, e.g. a+bi.

    Supports:
        str method
        add method
        subtract method
        divide method
        multiply method
        magnitude method
    """
    def __init__(self, real, imaginary):
        """ create complex number with the specified real and imaginary parts"""
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        """ format a string"""
        return "{} + {}i".format(self.real, self.imaginary)

    def __add__(self, other):
        """ add self and other """
        return Complex(self.real + other.real, other.imaginary + self.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        """
        Multiply two complex numbers.
            To multiply complex numbers, use distribution.
            (a + bi)(c + di) = ac + adi + bci + bdi^2
                             = ac + adi + bci - bd
                             = (ac - bd) + (ad + bc)i
        """
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real, imaginary)

    def __div__(self, other):
        """
        Divide two complex numbers.
            To divide complex numbers , multiply by the conjugate.
        """
        temp = self.__mull__(Complex(other.real, -other.imaginary))
        denom = other.real * other.real - other.imaginary * other.imaginary
        return Complex(temp.real/denom , temp.imaginary/denom)

num1 = Complex(2, 3)
num2 = Complex(-2, -3)
print(num1)
print(num2)
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print((2+3j) * (-2-3j))
#(2x + 3y)(4x + 6y)


class Customer:
    """
    Bank customers!
    """
    def __init__(self, name, num):
        self.name = name
        self.balance = num

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

cust1 = Customer("Brian", -100)
cust2 = Customer("Stephanie", -250)
cust1.withdraw(401)
cust1.deposit(80)
print(cust1.balance)
print(cust2.balance)
cust1.deposit(100 - cust1.balance)
cust2.deposit(250 - cust2.balance)
print(cust1.balance)
print(cust2.balance)

# Use a function to determine their current balances
# Update their balances using other functions so that cust1 ends up with $100
# and cust2 ends up with $250


# Make a pet store!
# Want animal objects... what are their states, their operations?
# We also want a pet store that has a selection of animals for customers
# to choose from. So what's its state? And what might a pet store have to do
# as operations, e.g. get more pets, feed a pet
