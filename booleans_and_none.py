# Booleans

# True or False

# a = True
# b = False

# print(a == b) # False
# print(a != b) # True
# print(a >= b) # True
# print(a <= b) # False
# print(b <= False) # True

# print(True and False) # False
# print(False and True) # False
# print(True and True) # True
# print(False and False) # False
#
# print(True or False) # True
# print(False or True) # True
# print(False or False) # False
# print(True or True) # True

# Booleans with datatypes

# hi = "Hello World!"
#
# print(hi.isalpha()) # checks if the string is alphanumeric - "Hello World!" returns false because of the space and "!"
# print(hi.islower()) # False
# print(hi.isupper()) # False
# print(hi.endswith("!")) # True
# print(hi.startswith("Hello")) # True

# x = 0
# y = 10
# z = -15
# print(bool(x)) #  False 0 is considered False
# print(bool(y)) # True

# None

# None == Null in a lot of other languages

print(bool(None)) # False

x = None
print(x == False) # False because None is an independent object like True or False

# Checking if a variable is 'None'

print(x == None) # direct comparison - not desirable in more complex situation
print(x is None) # best practice for checking if something 'is None'

print(type(x)) # <class 'NoneType'>







