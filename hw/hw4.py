import datetime

first_name = input("What is your first name?")
last_name = input("What is your last name?")
birth_year = int(input("What year were you born in?"))

current_year = datetime.datetime.now().year
age = current_year - birth_year
print(current_year)

print("Hello {}".format(first_name))
print("Hello {}".format(last_name))
print("You were born in {:08d}".format(birth_year))
print("The current year is {:.3E}".format(current_year))
print("That means you are ", age, "years old")
magicpercentage = birth_year / current_year
print("Your magic percentage is: {:.4f} ".format(magicpercentage))
