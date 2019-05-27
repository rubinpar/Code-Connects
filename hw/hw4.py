first_name = input("What is your first name?")
last_name = input("What is your last name?")
birth_year = int(input("What year were you born in?"))

print("Hello {}".format(first_name))
print("Hello {}".format(last_name))
print("You were born in {:08d}".format(birth_year))
print("The current year is 2.019e+03")
print("That means you are 18 years old")
birth = 2001
current = 2019
magicpercentage = birth % current
print("Your magic percentage is: ".format(magicpercentage))
