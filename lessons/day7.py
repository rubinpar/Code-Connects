# print 20, 22, 24, 26, and 28
# range(start, end, how many to add each time)
for number in range(20, 30, 2):
    print(number)

# how do you write this as a while loop?
i = 20
while i < 30:
    print(i)
    i = i + 2


# how many times does this run?
# 10
i = 10
while i > 0:
    print(i)
    i -= 1

# how many times does this run?
#
i = 10
while i < 40:
    print(i)
    i = i + 1

# i = 10, print 10, change i to 11
# i = 11, print 11, change i to 12
# i = 12,
# ... infinitely many times
# how do we get it to stop?

# how many times does this run?
i = 2
while i < 1000:
    print(i)
    i = i * i

# i = 2, print 2, i becomes 4
# i = 4, print 4, i becomes 16
# i = 16, print 16, i becomes 256
# i = 256, print 256, i becomes 65536


# print  0, -5, -10, -15, and -20.
for number in range(0, -21, -5):
    print(number)


# functions/methods
# problem:
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
#   we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def divisible_by_three(i):
    return i % 3 == 0
print(divisible_by_three(3))
print(divisible_by_three(5))

# divisible by five method
def divisible_by_five(i):
    return i % 5 == 0

def divisible_by_n(i, n):
    return i % n == 0

print(divisible_by_n(9, 4))

i = 0
total = 0
while i < 1000:
    # if divisible_by_three(i) or divisible_by_five(i):
    if divisible_by_n(i, 3) or divisible_by_n(i, 5):
        total += i
    i += 1

def sum_of_multiples(max_number, multiples):
    """
    max_number: when we end
    multiples: is a list of multiples to check for

    example: sum_of_multiples(100, [3, 5])
    """
    i = 0
    total = 0
    while i < max_number:
        if any([divisible_by_n(i, n) for n in multiples]):
            total += i
        i += 1
    return total
print(sum_of_multiples(1000, [3, 5]))
print(sum_of_multiples(100, [7]))
# list comprehension
print(["My name is {}".format(name) for name in ["Peter", "Paul", "Mary"]])
# def NAME(INPUTS):
#   do whatever we want
#   return OUTPUT (if we don't have a return statement it does return None)
