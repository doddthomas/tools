# ----------------------------------------------------------------------
#
#   supplies_append_insert_remove_ex.py - a python script showing list
#                                         example of append/remove/sort
#
#
# ---------------------    module history   ----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
# ----------------------------------------------------------------------


supplies = ['pens', 'grenades', 'flame-throwers', 'staples']
supplies.append('moose')
print(supplies)
# yields =>  ['pens', 'grenades', 'flame-throwers', 'staples', 'moose']

supplies.insert(2, 'inserted_2_value')
print(supplies)
# yields => ['pens', 'grenades', 'inserted_2_value', 'flame-throwers', 'staples', 'moose']

supplies.remove('inserted_2_value')
print(supplies)

supplies.sort()
print(supplies)
# yields => ['flame-throwers', 'grenades', 'moose', 'pens', 'staples']

spam = ['a', 'z', 'Z', 'A']
spam.sort()
print(spam)
# yields => ['A', 'Z', 'a', 'z']

spam.sort(key=str.lower)
print(spam)
# yields => ['A', 'a', 'Z', 'z']

# -------------- Logan Editions ----------------------------------------

# Pop can be used to remove an item based on index and store it in a variable
last_item = spam.pop(-1)
print(last_item)
# yields => 'z'

print(spam)
# yields => ['A', 'a', 'Z']

# If you want to retain the original list but still sort use ``sorted``
spam = ['a', 'z', 'Z', 'A']
sorted_spam = sorted(spam)
print(sorted_spam)
# yields => ['A', 'Z', 'a', 'z']

print(spam)
# yields => ['a', 'z', 'Z', 'A']

# Can also provide an anonymous function as a key for sorting
names = [('Trogdor', 'Burninator'), ('Logan', 'Thomas'), ('Dodd', 'Thomas'), ('Homestar', 'Runner')]
names.sort(key=lambda x: x[0])
print(names)
# yields => [('Dodd', 'Thomas'), ('Homestar', 'Runner'), ('Logan', 'Thomas'), ('Trogdor', 'Burninator')]

names.sort(key=lambda x: x[1])
print(names)
# yields => [('Trogdor', 'Burninator'), ('Homestar', 'Runner'), ('Dodd', 'Thomas'), ('Logan', 'Thomas')]
