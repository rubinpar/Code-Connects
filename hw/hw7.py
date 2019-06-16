# 1. write a function
# 2520 is the smallest number that can be divided
# by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?

<<<<<<< HEAD
def divisible_by_n(i, n):
    """
    i is divisible by n without a remainder
    """
    return i % n == 0

def divisible_1_thru_10():
    for i in range(1, 1000000):
        if i % 1 == 0:
            if i % 2 == 0:
                if i % 3 == 0:
                    if i % 4 == 0:
                        if i % 5 == 0:
                            if i % 6 == 0:
                                if i % 7 == 0:
                                    if i % 8 == 0:
                                        if i % 9 == 0:
                                            if i % 10 == 0:
                                                return i
print(divisible_1_thru_10())

def smallest_divisible_1_thru_x(x=20, max_number=1E8):
    number = 1
    while number < max_number:
        if all([divisible_by_n(number, i) for i in range(1, x+1)]):
            return number
        number += 1

print("Smallest number is ", smallest_divisible_1_thru_x(x=5))
# print(smallest_divisible_1_thru_x())


# 2. write another function
# Book Inventory
# Write a function called print_book that will print out the details of a book in
=======
# 2. write another function
# Book Inventory
# Write a function called printBook that will print out the details of a book in
>>>>>>> 3fa46c463b59aaf3e55673773e8b92d9f9f886ff
# a book stores inventory.
# Input Format
#
# The input parameters to your function should be the book title, author, num-
# ber of copies of the book, and price of the book.
#
# Constraints
# All the print statements need to happen inside the function. You should use
# the str() function to turn a number into a string.
# Output Format
# Print the book details in the format below. Also output the store revenue if
# they sell all the books in the inventory.
<<<<<<< HEAD
#
#
# EXAMPLE:
# Sample Input
# printBook("I Know Why the Caged Bird Sings", "Maya Angelou", 100, 20)
=======
# Sample Input
# printBook(”I Know Why the Caged Bird Sings”, ”Maya Angelou”, 100, 20)
>>>>>>> 3fa46c463b59aaf3e55673773e8b92d9f9f886ff
# Sample Output
# Title: I Know Why the Caged Bird Sing
# Author: Maya Angelou
# Number of Copies: 100
# Price per Copy: $20
# Revenue: $2000
#
# Explanation
# We print out out the title, author, number of copies, price per copy, and
# revenue on separate lines. The revenue is the number of copies multiplied by
# the price per copy, which is 2000.

<<<<<<< HEAD

# Name: print_book
# Inputs: name of the book [title], author, number of copies, price per copy
# Doing: calculate the revenue
# Outputs: No return, print stuff
def print_book(title, author, num_copies, price_copy):
    revenue = num_copies * price_copy
    print("Title: ", title)
    print("Author: ", author)
    print("Number of Copies ", num_copies)
    print("Price per Copy ", price_copy)
    print("Revenue: ", revenue)

print_book("I Know Why the Caged Bird Sings", "Maya Angelou", 100, 20)


# FizzBuzz game expert
# input: number to count up to
# outputs: Nothing, prints
# Example:
# FizzBuzz(15)
# Output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# Fizz buzz

def fizz_buzz(x):
    for i in range(1, x+1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz buzz")
        elif i % 3 == 0:  # NOT divisible by both 3  by 5
            print("Fizz")
        elif i % 5 == 0: # NOT divisible by 3
            print("Buzz")
        else:
            print(i)

fizz_buzz(15)


=======
>>>>>>> 3fa46c463b59aaf3e55673773e8b92d9f9f886ff
# 3. think about a project
