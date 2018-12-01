#-----------------------------------------------------------------------
#
#   del_items_from_list_ex.py - a python script showing examples of
#                               deleting items from a list
#
#---------------------    module history   ------------------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#   29-NOV-18 : PTR XXXX, Add .remove() and .pop() examples, Logan Thomas
#
#------------------------------------------------------------------------------

spam=['cat','bat','rat','elephant']
del spam[0]
print(spam)
#yields=>['bat', 'rat', 'elephant']

del spam[-1]
print(spam)
#yields=>['bat', 'rat']

# Can also delete by item name rather than index with .remove()
spam.remove('rat')
print(spam)
#yields=>['bat']

# If you'd like to store removed item and delete from list use .pop()
office_spam = ['dwight', 'bears', 'beets', 'battlestar galactiga']

# Defaults to popping last item in list
last_entry = office_spam.pop()
print(last_entry)
#yields=>'battlestar galactiga'

print(office_spam)
#yields=>['dwight', 'bears', 'beets']

# Can use .pop() with an index as well
second_item = office_spam.pop(1)
print(second_item)
#yields=>'bears'

print(office_spam)
#yields=>['dwight', 'beets']

