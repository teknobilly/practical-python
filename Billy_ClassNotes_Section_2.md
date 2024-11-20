\#  root /home/billy/Projects/2024/dabeaz </br>
\#  DaBeaz Python course</br>
\#  https://github.com/dabeaz-course/practical-python </br>
\# Billy's Pro-D to brush up on python for more Pro-d in AI/ML Application


# Section 2 - Working with Data
## Nov 17 2024 - Sunday 20:00

- Core Data Structures: tuples, lists, sets, and dictionaries
- Common data handling idioms
- Python's underlying object model

## Datypes and Data Structures

### Primitives
Basic types of primitives
- integers
- floating point numbers
- strings(text)

**None** type - # often used as a placeholder for optional missing value
```python
email_address = None

if email_address:  # result will be false
  send_email(email_address, msg)
```

### Data Structures
An object is a combination of primitives and other objects

ex `100 shares of GOOG at $490.10`
- Name or symbol of the stock ("GOOG" is a string)
- Number of shares (100) is an int
- Price (490.10) is a floating

### Tuples
A tuple is acollection of values grouped together
```python
s = ('GOOG', 100, 490.1)  # A Tuple
s = 'GOOG', 100, 490.1    # Also a tuple
s = ()                    # Empty tuple
s = ("GOOG", )            # 1 item tuple
```   

- Tuples are indexed like an array
- The contents can't be modified
```python
s = (s[0],75,s[2])  # You can copy the values to a new tuple
```
- Tuples are used to pack together items, often used to pass to functions

### Tuple Unpacking
Tuples can be unpacked into seperate variables:
```python
s = ('GOOG', 100, 490.1)
name, shares, price = s  # the tuple 's' is unpacked into variables
# The number of variables on the left MUST equal the number of 
#  values in the tuple
```
### Tuples vs Lists
Tuples look like read-only lists.  Tuples most oftern used for a single item consisting of multiple parts.  Lists are a collection of distinct items, usually all of the same type.
```python
record = ('GOOG', 100, 490.1)        # A tuple of a single entry
symbols = [ 'GOOG', 'AAPL', 'IBM' ]   # A List of same types
```
### Working with Tuples
Tuples are different from lists because they are immutable, or static.  Once created the values of table cannot be changed or appended.  Tuples are memory efficient ways of handling data.   

If data needs to be munged then the tuple() should be converted to a list()
Use the functions tuple() and list() to cast a container to another type:
```python
tuple_names   = ('first', 'second', '3rd', 4 )# A tuple
list_names    = list(tuple_names)     # the tuple is now a list in list_names.  Both exist.
list_names[3] = '4th'               # Munge the data
tuple_names  = tuple(list_names)    # the names tuple has been munged
```


### Dictionaries
Dictionaries are for holding key value pairs, one doesn't munge in a dictionary.  You can remove and add key:values.  There are dictionary methods for cleaning up dictionary entries.
Maps Keys and Values, aka Hash Table or Associative array
```Python
 s = {
    'name'    : 'GOOG',
    'shares'  : 100    ,
    'price'  : 490.1
 }
```

### Common Dictionary Operations
Use key names to retrieve values
```python
>>> print( s['name'], s['shares'] )
GOOG 100
```
Add or modify values in a similar way
` s['shares'] = 120`

Delete using the `del` keyword
` del s['date'] `

Dictionaries are useful when there are many different values and they might be manipulated.  They provide context and organization

### Exercises
> Is math broken in Python? What’s the deal with the answer of 3220.0000000000005?
> This is an artifact of the floating point hardware on your computer only being able to accurately represent decimals in Base-2, not Base-10. For even simple calculations involving base-10 decimals, small errors are introduced. This is normal, although perhaps a bit surprising if you haven’t seen it before.

Tuples are often used to pack and unpack values into variables
```python
>>> d = {  # d as in Dictionary
...     'name' : 'GOOG',
...     'shares': '100',
...     'price' : 490.10
... }
>>> list(d)  # list will output a list of keys
['name', 'shares', 'price']
>>> for k in d:   # k is an iterator 
...     print('k = ', k)
... 
k =  name
k =  shares
k =  price
>>> for k in d:
...     print(k, '=', d[k])  # dump the values of a Dictionary
... 
name = GOOG
shares = 100
price = 490.1
```
dict.keys() method  
- returns a dict_keys([ 'key1', 'key2' 'key3'])
- this is dynamically linked to the original dict
- if a key is deleted from the dict the dict_keys will represent that
dict.items() will return the dictionary in key,value pairs
- dict_items([('key1','value1'),('key2','value2'),('key3','value3)])
  
## Section 2.2 Containers 
Nov 17 2024 - 21:37:00
more lists, dictionaries, and now sets!

### Lists as a Container
Use a list of tuples to contain a CSV table
```python
portfolio = [
    ('GOOG', 100, 490.10),  # Tuple
    ('IBM',50,91.3),        # Tuple
    ('CAT', 150, 83.44)     # Tuple
] # A list of tuples
```

### List Construction
Build a list of tuples iterativly like
```python
records = []  # Initial empty List

# use .append() to add items
records.append( ('GOOG', 100, 490.10) )  # A tupple is added to a list
records.append( ('IBM', 150, 91.30) )  # A tupple is added to a list
```

Build a list with values from a CSV
```python
records = []

with open('Data/portfolio.csv', 'rt') as f:   # Read from text file
    next(f)  # Skip Header row
    for line in f:
        row = line.split(',')
        records.append( (row[0], int(row[1]), float(row[2])))
```

### Dicts Construction
Dictionaries are usefull if you want fast random lookups by key name
```python
prices = {}  # Init empty dict

prices['GOOG'] = 513.25
prices['CAT']  = 87.22
prices['IBM']  = 93.37
```
Building dict from CSV file:
```python
prices = {}  # Init prices dict

with open('Data/prices.csv', 'rt') as f:
    for line in f:                # Read line
        row = line.split(',')     # splist the CSV
        prices[row[0]] = float(row[1])   # append Key = Value pair 
        # When defining Key = Values use an = not colon
```

### Dictionary Lookups
```python 
if key in d:
    # True
else: 
    # False
```

`dict.get(key, default) ` Use a default value incase there is no value

### Sets
Sets are collection of unordered unique items.  Sets are for unique entries.   You would not store data in sets, more likely for a list of tags, or column names.  Set items can be added, removed, joined, intersected, and differenced.

```python
tech_stocks = { 'IBM', 'AAPL', 'MSFT' }
# Alternative syntax
tech_stocks = set( ['IBM', 'AAPL', 'IBM' ] )
```
When initializing sets use `aset = set()` rather than empty `dict = {}`
Sets will remove all duplicate items by default
Sets have methods for organizing
```python
s = { 1, 2, 3 }  # a set
s.add(4)  # add 4 to the set
s.add(4)  # 4 is already in set.   Will not add a second
s.remove(4) # 4 is remove
s.remove(4) # ERROR! there is no 4
s.discard(4) # no error, will ignore
```

### Set Union
Join two sets together
```python
s1 = { 1, 2, 3 }
s2 = { 3, 4, 5 }
s3 = s1.union(s2)  # or shortform  s1 | s2 
s3
# {1, 2, 3, 4, 5}  #notice no second 3
```
**More** from [PythonCheatsheet.org](https://www.pythoncheatsheet.org/cheatsheet/sets)
- Set Intersection
- set Difference
- set symmetric_difference

*That's all for tonight folks!*  22:10:00 Nov 17 2024

## Section 2.3 - Formating with f-strings
Use f-strings to format data output into tables in a cli shell

### Formating codes in strings
```python
>>> cats = ['Rusty', 'Opie', 'Chico', 'Pepper', 'Panda']        # A list of cats
>>> for index,name in enumerate(cats):                         # pulling index with enumerate()
...     print(f'# My {index:>3d}st Cat\'s name was {name:<10s}')  # Formatted printing
... 
# My   0st Cat's name was Rusty     
# My   1st Cat's name was Opie      
# My   2st Cat's name was Chico     
# My   3st Cat's name was Pepper    
# My   4st Cat's name was Panda 
```

There are various codes you can use to format an output field
```
 s - String
 c - char
 d - decimal integer (ints)
 b - binary
 x - Hexadecimal
 f - Float [-]00.000...
 e - Float [-]00.00000+-xx
 g - Floar, but with E notation
```
and field modifiers
```
:>10d - field is 10 wide, type integer, aligned to right
:<10d - field is 10 wide, type integer, aligned left
:^10d - field is 10 wide, type integer, centered in field
:10.2f - field is 10 wide, with 2 decimal point precision
```

[C++ fprint() formating is also available](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)

















































  
# fin
