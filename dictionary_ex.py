# -----------------------------------------------------------------------
#
#   dictionary_ex.py - a python script showing examples of dictionary
#                      key-value pairs
#
#
# ---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
# -----------------------------------------------------------------------


# dictionary denoted by braces and key-value pair
myDog = {'size':'fat', 'color':'orange', 'disposition':'no_bark'}
print(myDog)
print(myDog['color'])

for v in myDog.values():
    print(v)

for k in myDog.keys():
    print(k)

for i in myDog.items():
    print(i)

if myDog.get('color',0) != 0:
    print('color is a key value in the dictionary')
else:
    print('color is NOT a key value in the dictionary')

# Examples of grabbing an item from a dict based on key
print(myDog['size'])
# yields => fat

print(myDog['name'])
# yields => KeyError
# # ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-4-b7572bd41768> in <module>
# ----> 1 print(myDog['name'])
#
# KeyError: 'name'

print(myDog.get('name'))
# yields => None

print(myDog.get('name', 'Not Found'))
# yields => Not Found

# Examples of iterating over a dict
for key,value in myDog.items():
    print(key)
# yields =>
# size
# color
# disposition

for key,value in myDog.items():
    print(value)
# yields =>
# fat
# orange
# no_bark

for entry in myDog.items():
    print(entry)
# yields =>
# ('size', 'fat')
# ('color', 'orange')
# ('disposition', 'no_bark')

for i, (k,v) in enumerate(myDog.items()):
    print(f'Index {i}: Key: {k} Value: {v}')
# yields =>
# Index 0: Key: size Value: fat
# Index 1: Key: color Value: orange
# Index 2: Key: disposition Value: no_bark

# -----------------------------------------------------------------------

# OrderedDict Example
#     In older versions of Python, a dictionary would be sorted by key
#     For example, in Python 2.7 the below would be true:
myDog = {'d':4, 'b':2, 'a':1, 'c':3}
print(myDog)
# yields => {'a': 1, 'c': 3, 'b': 2, 'd': 4}

# For this reason, Python has a built in OrderedDict class
from collections import OrderedDict

myDog = OrderedDict([('d',4), ('b',2), ('a',1), ('c',3)])
print(myDog)
# yields => OrderedDict([('d', 4), ('b', 2), ('a', 1), ('c', 3)])

# Yuck... pretty messy...

# Good news is that any version of Python post 3.6 automatically orders
# dictionary values based on instantiation order.

# Python 3.6 and on
myDog = {'d':4, 'b':2, 'a':1, 'c':3}
print(myDog)
# yields => {'d': 4, 'b': 2, 'a': 1, 'c': 3}

# -----------------------------------------------------------------------

# Another powerful dict tool built into Python is the default dict
# Let's go through a few examples:

# Example 1: Collecting instead of overriding
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = {}  # ordinary dict defn
for k,v in s:
    d[k] = v
print(d)
# yields => {'yellow': 3, 'blue': 4, 'red': 1}

from collections import defaultdict

d = defaultdict(list)  # all keys are instantiated as an empty list
for k,v in s:
    d[k].append(v)
print(d)
# yields => defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})

# This is also useful for counting things
s = 'mississippi'
d = defaultdict(int)  # all keys are instantiated as an int and starts as 0
for k in s:
    d[k] += 1
print(d)
# yields => defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})

# -----------------------------------------------------------------------

# Side Note... if you wanted to count the letters in mississippi, Counter is better
from collections import Counter
print(Counter(s))
# yields => Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
# Notice prints in order of most occurring

# -----------------------------------------------------------------------
# Example 2: Default value (different that .get()

ice_cream = defaultdict(lambda: 'Vanilla')

ice_cream['Yeager'] = 'Chunky Monkey'
ice_cream['Logan'] = 'Rocky Road'

print(ice_cream['Cindy'])
# yields => Vanilla

# Notice that Cindy is added to ice_cream dict with default value
print(ice_cream)
# yields => defaultdict(<function <lambda> at 0x7ffe31119170>, {'Yeager': 'Chunky Monkey', 'Logan': 'Rocky Road', 'Cindy': 'Vanilla'})

print(ice_cream.get('Dodd'))
# yields => None

# Notice that Dodd is not added to ice_cream dict
print(ice_cream)
# yields => defaultdict(<function <lambda> at 0x7ffe31119170>, {'Yeager': 'Chunky Monkey', 'Logan': 'Rocky Road', 'Cindy': 'Vanilla'})
