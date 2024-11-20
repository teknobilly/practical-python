\#  root /home/billy/Projects/2024/dabeaz </br>
\#  DaBeaz Python course</br>
\#  https://github.com/dabeaz-course/practical-python </br>
\# Billy's Pro-D to brush up on python for more Pro-d in AI/ML Application


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

# [Sect 1.4 Strings](https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/04_Strings.html)
Nov 16 20:52 - Dinner, and futzing about with the mortgage program.   I could get my results to match his. I think I'm right ;)
- 22:00:00 spect couple hours looking a GPU options  Going to bed
Nov 17 12:00 - Still Sick, Pokemond Tanya, ordered new Pro-D System components
- Goal, get through 1 and work on 2

Wonderful world of strings

### Quotes
- \' \' - single quotes are the same as \" \" - double quotes
  - but they must5 be used as a set,
  - you can use quotes in strings by alternating single with double, or escaping the quote \\"
- \'\'\' Triple quotes are like Markdown they will contain a block of text, returns and all

### Escape Codes
- The usual escape codes exist

### String Representation
- a code-point is the digit representation of the character in the string
- specify code-points as follows
```python
a = '\xf1'          # a = 'ñ'
b = '\u2200'        # b = '∀'
c = '\U0001D122'    # c = '𝄢'
d = '\N{FOR ALL}'   # d = '∀'
```
- [unicode character database](https://unicode.org/charts)

### String Indexing
- Strings are arrays, they start at 0
```python
a = 'Hello world'
b = a[0]  # H
c = a[4]  # o
d = a[-1] # d - end of string
```
- Slice it
```python
d = a[:5]   # Hello - from the begining
e = a[6:]   # world - from the end
f = a[3:8]  # lo wo - not that it does not include the 8th character. I would think it should
```

### String Operations
- Concatenating Strings with the + operator
` a = 'Hello' + 'world!' `
- Length function
` x = len(a) `
- operators `in` and `not in`
```python
t = 'e' in a      # True
f = 'x' in a      # False
g = 'hi' not in a # True
```
- Replication *
` rep = a * 5    # 'Hello world!Hello world!Hello world!Hello world!Hello world!'  `

### String Methods
- strip all spaces in string
```python
s = '   Hello  '
t = s.strip()  #  'Hello'
```
- Replacing text
```python
s = 'Hello wold!'
t = s.replace('Hello', 'Wonderful') #  'Wonderful word!'
```
- More string methods
```python
 s.endswith('suffix')  # Check if string ends with 'suffix'
 s.find('text')       # First occurance of 'text' in s
 s.index('x')         # returns first position of 'x' in string
 s.isalpha(str)
 s.isdigit(str)
 s.islower(str)
 s.isupper(str)
 s.join(slist)   
 s.lower(str)
 s.replace(old, new)
 s.rfind(char)         # Find first from end
 s.rindex(char)        # return Index of char in string
 s.split([delim])      # Split string into list of substrings
 s.startswith(prefix)  # Confirms if string starts with prefix
 s.strip()              # Clears leading trailing spaces
 s.upper()             # Convert to uppercase
```

### String Mutability
- Strings are immutable!
```python
s = 'Hello world!'
s[1] = 'a'  # Results in type error
```
- All operations and methods that manipulate string data, alwasy create new strings

### String Conversions
- use `str()` to convert any value to a string

### Byte Strings
- a byte string is an ascii string, not unicode
- byte strings work with most string methods
- byte strings indexs will return the Ascii Value, not the character
- Convert to from text strings  ( 'ascii' , 'latin1', 'utf-8' )
```python
text = data.decode('utf-8')  # bytes -> text
data = text.encode('utf-8')  # text -> bytes
```

### Raw Strings
- good for pathnames and regular expressions
```python
rs = r'c:\newdata\test'  #  Raw ininterpreted backslashes
>>> rs
'c:\\newdata\\test'
```

### f-strings
- Formatting strings for column mode output
```python
>>> shares=100
>>> price =91.1
>>> b = f'Cost = ${shares*price:0.2f}'
>>> b
'Cost = $9110.00'
```

### Regular Expressions
- need to import module re
```python
>>> text = 'today is 11/17/2024.  Tomorrow is 11/18/2024.'
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'today is 2024-11-17.  Tomorrow is 2024-11-18.'
>>> re.findall( r'\d+/\d+/\d+', text )
['11/17/2024', '11/18/2024']
```
[Regular Expressions documentation](https://docs.python.org/library/re.html)

**Discovering supported methods
- In the Python cli you can use `>>> dir(str)` to see a list of methods support by that variable
- Also use `>>> help(str.upper)` to get more information on methods

# 1.5 Lists - 14:18 Sunday Nov 17
### Pythons primary type for holding an ordered collection of values
Lists are most like an array from javascript.   Arrays in Python can only contain one data type.  Where as lists and tuples can hold anything.  Lists of tuples for example.

Lists also have many operation methods for working with the data.  Review the Python cheatsheet when working on munging lists.

### Creating a List
```python
names = [ 'Elwood', 'Jake', 'Curtis']
nums = [39, 38, 42, 65, 111 ]
```

### Parsing a string into a list
- Use split to turn csv to a Python List
```python
>>> line = 'GOOG,100,490.10'
>>> row = line.split(',')
>>> row
['GOOG', '100', '490.10']
```

### List operations
``` python
# Adding list items
names.append('Murphy')    # Adds list item to end of list
names.insert(2, 'Aretha')  # Adds list item to front of list

# Concatenating lists
>>> s = [1,2,3]
>>> t = ['a','b','c']
>>> s + t
[1, 2, 3, 'a', 'b', 'c']

# Lists are indexed like arrays starting at 0
names[0]  # 'Murphy'
names[1]  # `Elwood`
names[-1] # 'Aretha'

# List Length
len(names)  # 5

# Membership Test
'Ellwood' in names  # True
'Britney' in names  # False

# Replication
>>> s = [1,2,3]
>>> s * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### List Iteration and Search
- use: 
```python
for *value*  in *List*:
  print(value)
```

### List item removal
- Odd, use: del 
```python
# Using the Value
names.remove('Curtis')

# Using the index
del names[3]
```

### Sorting Lists
```python
s = [10,1,7,3]
s.sort()  # [1,3,7,10]
```
### Joining Lists
```python
>>> s = [1,2,3]
>>> str_numbers = []
>>> for i in s:
...   str_numbers.insert(0,str(i))
... 
>>> str_numbers
['3', '2', '1']
>>> '-'.join(str_numbers)
'3-2-1'  # The int list is now a string
```

### Lists of Anything
- Lists of int
- Lists of str
- lists of float
- list of list
- they can be joined with each other
- **Warning** - Lists of different types are a bad idea

### Lists vs Tuples
In section 2.  I review tuples and show how the two differ.

# Section 1.6 - File Management - Nov 17 15:23:00  
### Open a file
```python
f = open('foo.txt', 'rt')   # Open for reading (Text)
g = open('bar.txt', 'wt')   # open for writing (text)
```

### Read File
```python
filedump  = f.read()
filechunk = f.read(1024)

# Write Text to file
f.write('text writing to file')

# Close the files
f.close()
# OOPS! I forgot to close g
g.close()
```

### Common idioms for reading a file
Use the with command for reading files, this is a safer way of reading files.   When the with block is done the file will close automatically. 
>This is because the with statement calls 2 built-in methods behind the scene – __enter()__ and __exit()__.
>The __exit()__ method closes the file when the operation you specify is done.
```python
# Read whole file as string
with open('foo.txt', 'rt') as file:
  data = file.read
  # 'data' is a string with all the text in 'foo.txt'
  
# Read file line by line
with open('foo.txt', 'rt') as file:
  for line in file:
    # process the line
```

### Common idioms for writing a file
```python
# contents from string appended to file
with open(outfile.txt', 'wt') as out:
  out.write('hello world\n')
  
# another way to append a file
with open('outfile.txt', 'wt') as out:
  print('Hello world.', file=out)
  
```

## Exercises 

### OS Operations provided by module os
```python

```

# Section 1.7 - Functions - Nov 17th 16:28
- 18:56:00  After Dinner

### Custom Functions

```python
>>> def sumcount(n):
...     '''
...     Returns the sum of the first n integers
...     '''
...     total = 0
...     while n > 0:
...         total += n
...         n -= 1
...     return total
... 
>>> sumcount(4)
10
```
- The keyword def, is that define

### Library Functions - Modules?
- [Python has a large std Library](https://docs.python.org/3/library/index.html)
- Pythons Standard Library Modules
    [Copy, Datetime, Itertools, Json, Os, Pathlib, Random, Shelve, Zipfile]
- Modules are imported into a script, Globally or locally
` import math `

### Errors and Exceptions
- Functions report erros as exceptions.
```python
>>> int('N/A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'N/A'
```
- The default behaviour dumps the running script and displays the error information

### Catching and handling Exceptions
- try: except:  
```python
>>> def divide(dividend, divisor):
...     try:
...             print(dividend / divisor)
...     except:
...             print('You cannot divide by 0')
... 
>>> divide(dividend=10,divisor=5)
2.0
>>> divide(dividend=5, divisor=10)
0.5
>>> divide(dividend=5, divisor=0)
You cannot divide by 0
```
- Python has many types of errors: [Built-in exceptions](https://docs.python.org/3/library/exceptions.html)

### Raising Exceptions
```python
>>> raise RuntimeError('What a kerfuffle')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: What a kerfuffle
```

### Using Library Functions - csv
```python
>>> import csv
>>> f = open('Data/portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)  # Next is a function> next(iterator) - An iterator is an Object
>>> headers
['name', 'shares', 'price']
>>> for row in rows:
...     print(row)
... 
['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
```
Note: sys.argv is a list containing the passed arguments from the command line
` filename = sys.argv[1] `


















































  
# fin
