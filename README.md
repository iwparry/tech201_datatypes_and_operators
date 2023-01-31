# Tech 201 - Python Data Types and operators
Python contains several data types and operators that are used in our code.
## Data Types
Data types include the following:
### Numeric
First of all we have Integers, which are simply whole numbers, for example
```
int_num = 4
print(type(int_num))         # returns <class 'int'>
```
The other commonly used numeric datatype are floating point numbers, which are any real numbers that can be represented with a decimal point, here's an example of a float in Python
```
float_num = 3.4
print(type(float_num))       # returns <class 'float'> 
```
### Strings
Another data type in Python is a 'String', simply put, a string can be text of any kind contained within single or double quotations
```
my_string = "Hello World!"
print(type(my_string))       # returns <class 'str'>
```
### Boolean
A very simple and incredibly useful data type in Python is a Boolean which has two value `True` or `False`
```
my_bool = True
print(type(my_bool))         # returns <class 'bool'>
```
## Operators
Python has several operators which we can utilise when writing our code
### Arithmetic
These are standard mathematical operators including addition, subtraction, multiplication and division as shown below
```
x = 2
y = 4
add = x + y                  # returns 6
sub = x - y                  # returns -2
mult = x * y                 # returns 8
div = x / y                  # returns 0.5
```
### Comparison
Comparison operators are useful because what they do is evaluate if statements are `True` or `False`, the comparison operators are as follows
```
a = 1
b = 2
a == b   # a is equal to b - False  
a != b   # a is not equal to b - True
a >= b   # a is greater than or equal to b - False
a <= b   # a is less than or equal to b - True
a > b    # a is greater than b - False
a < b    # a is less than b - True
```