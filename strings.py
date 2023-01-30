# Strings

# single_quotes = 'Look! Single quotes'
# double_quotes = "Look! Double quotes"
#
# print(single_quotes)
# print(double_quotes)
# # string_failure = 'I said 'wow''
#
# escape_example = 'I said \'wow\''
#
# print(escape_example)
#
# quote_in_quote = 'I said "Wow"'
# print(quote_in_quote) # works the other way round "I said 'Wow'" will still print

# String slicing

# Everything in code starts at 0 index

# H e l l o   w o r l d !
# 0 1 2 3 4 5 6 7 8 9 1011

# hw = "Hello World!"
# print(hw[7:]) # orld!
# print(hw[-5:]) # orld!
# print(hw[:5]) # Hello
# print(hw[0:5]) # Hello
# print(hw[-6:-1]) # World
#
# # String Methods
#
# # strip() removes all white space at the end of a string
#
# whitespace = "lot's of space at the end                             "
# print(len(whitespace)) # 54
# strip_wp = whitespace.strip() # applying the method to our whitespace string
# print(len(strip_wp)) # 25
#
# # A few more
#
# example_text = "Here's some text with lots of text"
#
# # count() counts how many instance of an argument appears in the string
#
# print(example_text.count('text')) # 2
#
# # lower()
# print(example_text.lower()) # here's some text with lots of text
#
# # upper()
# print(example_text.upper()) # HERE'S SOME TEXT WITH LOTS OF TEXT
#
# # capitalise
# print(example_text.capitalize()) # Here's some text with lots of text
#
# # replace - replaces all instance of one argument with a new argument
# print(example_text.replace('with', ',')) # Here's some text, lots of text
#
# # Concatenation adds strings together
# a = 'here '
# b = 'more '
# c = 'much more'
# print(a + b + c) # here more much more
#
# # Casting
# x = 2
# y = 5.4
# z = " there's a number 25.4 unless we put a space!"
# # print(x + y + z) doesn't work because we cannot operate on numerical datatypes and strings!
#
# print(str(x) + str(y) + z) # 25.4 there's a number 25.4 unless we put a space!
#
# # string to numeric
#
# istring = "6"
# fstring = "3.5"
# print(int(istring))
# print(type(int(istring))) # <class 'int'>
# print(float(fstring))
# print(type(float(fstring))) # <class 'float'>

# F-strings = Formatted strings, do this via f"string" and use {variable}

# name = "Lassie"
# age = 7
# height_cm = 60.2
#
# print(f"{name} is {age} years old and is {height_cm}cm tall.") # puts the variables into the desired string
# print("{} is {} years old and is {}cm tall.".format(name, age, height_cm)) # returns the same as previous line

# F-strings allow us to use methods/evaluations

name = "Snoopy"
age = 52
print(f"{name.upper()} IS {age * 7} OLD IN DOG YEARS!!!")

# F-string to specify precision in rounding and decimals

pi = 3.14159265359

print(f"Pi to 3 decimal places: {pi:.3f}") # Pi to 3 decimal places
print(f"Pi to 3 decimal places: {pi:.5f}") # Pi to 3 decimal places

score = 16
max_score = 26

print(f"You scored: {score / max_score}") # 0.6153846153846154
print(f"You scored: {score / max_score:%}") # 61.538462%
print(f"You scored: {score / max_score:.2%}") # 61.54%
print(f"You scored: {score / max_score:.0%}") # 62%