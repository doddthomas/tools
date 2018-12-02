"""
Typically, a module has a description at the top giving a brief summary
of its functionality and/or some examples. This is housed in a `docstring`
(a block of text surrounded by three double quotation marks). Below is an
example of what I would write for this script:

Examples of how to print objects in Python.

This script demonstrates a few methods for printing objects in Python.

Topics covered:
    - %-formatting
    - str.format()
    - f.strings

TODO:
    * Code review this type of documentation.
    * Remove below doc and replace with this. Or, vice versa.
"""

#-----------------------------------------------------------------------
#
#   print_ex.py - a python script showing examples of printing
#                 objects in Python.
#
#---------------------    module history   -----------------------------
#
#   01-DEC-18 : PTR XXXX, Created, Logan Thomas
#
#-----------------------------------------------------------------------

# Define dummy objects to print
name = 'Tina'
age = 35
hams = 2.5

# Old-school string formatting in Python: %-formatting
# This is not recommended by the official Python docs
print('Hello %s' % name)
# yields => 'Hello Tina'

print('Hello %s. You are %d years old and have eaten %.2f hams today.' % (name, age, hams))
# yields => 'Hello Tina. You are 35 years old and have eaten 2.50 hams today.'



# More recent string formatting (preferred instead of %-formatting)
print('Hello {}'.format(name))
# yields => 'Hello Tina'

print('Hello {}. You are {} years old and have eaten {} hams today.'.format(name, age, hams))
# yields => 'Hello Tina. You are 35 years old and have eaten 2.5 hams today.'

# Can switch indexes to print with str.format
print('Hello {0}. You are {2} years old and have eaten {1} hams today.'.format(name, age, hams))
# yields => 'Hello Tina. You are 2.5 years old and have eaten 35 hams today.'



# Most recent (Python 3.6 and above) and most preferred: f-strings.
print(f'Hello {name}')
# yields => 'Hello Tina'

print(f'Hello {name}. You are {age} years old and have eaten {hams} hams today.')
# yields => 'Hello Tina. You are 35 years old and have eaten 2.5 hams today.'

# f-strings support arbitrary expressions
print(f'{5*3}')
# yields => 15

# f-strings support function evaluations
def shout(name):
    return name.upper() + '!!!'


print(f'{shout(name)} Eat your food!')
# yields => 'TINA!!! Eat your food!'

