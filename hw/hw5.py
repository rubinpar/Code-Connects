# HW:
# 1. Print the odd numbers between 0 and 40 using variables to store 40
#      and some kind of loop
#      (2 different ways, maybe using range, for loop, a while loop)
# 2. Add your two favorite numbers and then print the remainder when you divide
#    that sum by your age. For example, if your favorite numbers were 1 and 2
#    and you were 2 years old, you would print the number 1.
#    Remember to use varaibles.

number = 40
for index in range(40):
    print(index)

lower = 0
upper = 40
for i in range(lower,upper+1):
    if i % 2 != 0:
        print(i)

start, end = 0, 40
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num)
print("----------")

number = 1
while number < 40:
    print(number)
    number = number + 2

start, end = 0, 40
for number in range(start, end, 2):
    print(number)

#while CONDITION:
#  # (Condition is true or false and continues until the condition is false)
#   DO STUFF


fav_number = 9
fav_number2 = 20
print(fav_number + fav_number2)
age = 18
print(fav_number + fav_number2 % age)
