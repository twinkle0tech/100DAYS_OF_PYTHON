

# TIPS CALCULATOR PROJECT






# learned on 2 day


<!-- DATA TYPES -->
-primitive data type inpython
1)string
2)integers
3)floats
4)booleans

# Subscripting
print("Hello"[0])

# String
print("123" + "345")

# Integer = Whole number
print(123 + 345)

# Large Integers
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)

---

<!-- TYPE ERROR , TYPE CHECKING AND TYPE CONVERSION -->

TypeError
These errors occur when you are using the wrong data type. e.g. len(12345)

Because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you give it a number (Integer).

PAUSE 1. Fix the len() function so it has no more warnings or errors.

# TypeError
# len(123)

# No TypeError
len("Hello")

---

Type Checking
You can check the data type of any value or variable in python using the type() function.

print(type("abc")) #will give you <class 'str'>

# Type Checking
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

---

Type Conversion
You can convert data into different data types using special functions. e.g.

float()

int()

str()
# Type Conversion
str()
int()
float()
bool()

name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))  # str
print(type(length_of_name))  # int

print("Number of letters in your name: " + str(length_of_name))

---

<!-- MATHEMATICAL OPERATION -->
Basic Operators
Learn to use the basic mathematical operators, +, -, *, /, // and **

PEMDAS
Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3)
print(2 ** 3)

# PEMDASLR Order
# ()
# **
# * OR /
# + OR -

<!-- NUMBER MANIPULATION -->

## Flooring a Number
You can floor a number or remove all decimal places using the int() function which converts a floating point number (with decimal places) into an integer (whole number).

int(3.738492) # Becomes 3

## Rounding a Number
However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. Then you can use the python round() function.

round(3.738492) # Becomes 4

round(3.14159) # Becomes 3

round(3.14159, 2) # Becomes 3.14

## Assignment Operators
Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.

+=

-=

*=

/=

## f-Strings
In Python, we can use f-strings to insert a variable or an expression into a string.

age = 12

print(f"I am {age} years old")

# Will output I am 12 years old.