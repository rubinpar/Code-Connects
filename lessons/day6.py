A = True
B = True
C = False
D = True
E = False

print(type(A))
print(A and B)   # True
print(A and C)   # False
print(D and E)   # False
print(D or E)    # True
print(not A)     # False
print(not not A) # True

# And: takes two inputs and outputs the when they're both true
# A     |    B   | outputs
# ----------------------------
# True  |   True | True
# True  |  False | False
# False |  True  | False
# False | False  | False

# Or: takes two inputs and outputs when at least one of them is true
# A     |    B   | outputs
# ----------------------------
# True  |  True  | True
# True  |  False | True
# False |  True  | True
# False | False  | False

# not: takes one input and output the opposite
# not True == False
# not False == True
