/# root /home/billy/Projects/2024/dabeaz
/# DaBeaz Python course
/# https://github.com/dabeaz-course/practical-python

# Nov 16 2024 - Sat
Objective:Brushing up on my pySkillz so I can use PyTorch somewhat more competently that I can now
- This course is free and I found it referenced from the Python site.

[00_Setup](https://dabeaz-course.github.io/practical-python/Notes/00_Setup.html)
12:00:00
## Requirements
Python 3.6 or newer.  Oldblue has 3.12 which is newer

### IDE - Kate
I will install Kate IDE
- needed to install MarkDownPart package to get MD "Document Preview" to work
But first I have to update oldBlue...

# [1.1 Python](https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/01_Python.html)

- Python CLI interactive
```
>>> print("hello world!")
  # Prints Hello World
```

-Math in PYthon Cli
```
>>> (75 * 235.14) - (75 * 711.35)
  # result prints 35708.25
  - Underline _ is a pointer to the last result
>>> _ * 0.80
  # result: 28566.6000000000002
```
## Exercise 1.2 Help() CLI
In cli mode use `help()` to enter Help mode.
`help> ` 
- then type in the keyword you need help on.   You can get a list of keywords and modules, Symbols, or topics
ex:
```
help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or                  None                continue            
...
```

[Python 3.12 documentation](https://docs.python.org/3.12/)

## Exercise 1.3 - 1:51  (Effin around with Kate)
 - Basic CLI math statements
 
## Exercise 1.4
 - The example from the text doesn't work. the URL is no longer valid.   So I tried http://lite.cnn.com which didn't work either, but the URL is valid
 - [Python Doc Cli](https://docs.python.org/3.12/tutorial/introduction.html)
 - Not able to get this working ElementTree did not like the URL

# 1.2 First Program
Interactive Mode
- Running Python opens interactive mode
> REPL Read-Eval-Print-Loop

Creating Programs
- Python programs use the `.py' extension

Running Programs

`#> python hello.py `

A Sample Program
Let’s solve the following problem:
> One morning, you go out and place a dollar bill on the sidewalk by the Sears tower in Chicago. Each day thereafter, you go out double the number of bills. How long does it take for the stack of bills to exceed the height of the tower?

- created ./Work/sears.py and ran with python
- Note: Use sheBang on first line to python exec 
`#!/usr/bin/python`

Statements
- Each line is a statement in Python

Comments
- use # to start a comment.  Inline works as well

Variables
- can be named with [_[A-Za-z][1..9]]
- a digit cannot be the first character
- Only underscore is allowed.  no hyphens!

Types
- Variable type do not have to be declared.  Dynamically typed
```python
height = 442              #int
height = 442.0            #Float
height = 'Really Tall!'   #String
```
 
Case Sensitivity
- Yes

Looping
- While Loop runs as long as first statement is true
- ... [also has else](https://docs.python.org/3.12/reference/compound_stmts.html#while)
```python
while num_bills * bill_thickness < sears_height:
  print(day, num_bills, num_bills + bill_thickness)
  day = day + 1
  num_bills = num_bills * 2
  
print('Num of days', day)
```

Indentation
- used to denote a group of statements belong together

Indentation Best Practices
- use spaces instead of tabs
- use 4 spaces per level
- use a python aware editor

Conditionals
- if statement is used for Conditionals
```python
if a > b:
    print('computer says no')
else:
    print('computer says yes')
```

Printing
```python
print('hello world!') # Prints the text hello world
x = 100
print(x)              # prints the text 100
name = "Jake" 
print(name)           # Prints the text Jake
print("Hello ", name ) # prints Hello Jake \r\n
print("hello ". end=' ')  # does not end with \r\n
```

User Input
- input() function
```python
name = input('Enter your name:')
print('your name is', name)
```

Pass Statement
- Used to skip an indented block
if a > b:
    pass
else:
    print('Computer says false')
    
## Exercises
Exercise 1.5 - The bouncing ball
- Wrote Work/bounce.py to test the exercise.   Works!

# Section 1.3 Numbers
Math calculations

Types of numbers
- booleans - True=1 and False=0
- integers - (int) whole numbers + / -
```python
a = 37
b = -123491823748127349127341234018723498
c = 0x7fa8     # Hexidecimal
d = 0o253      # Octal
e = 0b10001111 # Binary
```
- floating point
```python
a = 37.45
b = 4e5 # 4 x 10**5 or 400,000
c = -1.345e-10
```
- complex (Imaginary Numbers)

Operators
```python
x + y   # addition
x - y   # subtraction
x * y   # multiplication
x / y   # division
x // y  # Floor divide (Produces integer)
x % y   # Modulo  (remainder (float))
x ** y  # Exponential Power
x << n  # bit shift left n times
    >>> x = 0b1
    >>> x << 1
    2
    >>> x << 2
    4
x >> n  # bitshift right n times
x & y   # bitwise AND
x | y   # bitwise OR
x ^ y   # bitwise XOR
~x      # bitwise NOT
    x = 5      # binary: 0101
    y = 3      # binary: 0011
    z = x & y  # binary: 0001, decimal: 1
abs(x) # Absolute value
x and y == x && y # Logical AND operators
x or y == x || y  # Logical OR operators
x = 1   # Assignment operators
x == y  # Equal to Comparison operators
```
**note:** [bitwise operators are not logical operators](https://medium.com/@saverio3107/pythons-logical-vs-bitwise-operators-e5453a9b3649)

Math Module for floating point operators
```python
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)
```

Comparison Operators
```python
x < y
x <= y
x > y
x >= y
x == y 
x != y
x and y
x or y
not x
```
Converting Number Variable Types
```python
a = int(x)
b = float(x)
```
## Exercises 17:25:00 
1.7 - Daves Mortgage















































  
# fin
