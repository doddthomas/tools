# -----------------------------------------------------------------------
#
#   supplies_list_range_ex.py - a python script showing example using
#                               range in lists
#
# ---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#   01-DEC-18 : PTR XXXX, added enumerate() example, Logan Thomas
#
# -----------------------------------------------------------------------

supplies = ['pens', 'grenades', 'flame-throwers', 'staples']
for i in range(len(supplies)):
    print('INDEX=> ' + str(i) + ' in supplies is: ' + supplies[i])

# yields=>
# INDEX=> 0 in supplies is: pens
# INDEX=> 1 in supplies is: grenades
# INDEX=> 2 in supplies is: flame-throwers
# INDEX=> 3 in supplies is: staples

# More pythonic approach is to use  enumerate()
supplies = ['pens', 'grenades', 'flame-throwers', 'staples']
for i,item in enumerate(supplies):
    print('INDEX=> ' + str(i) + ' in supplies is: ' + item)

# yields=>
# INDEX=> 0 in supplies is: pens
# INDEX=> 1 in supplies is: grenades
# INDEX=> 2 in supplies is: flame-throwers
# INDEX=> 3 in supplies is: staples

# Can also specify starting index with enumerate()
supplies = ['pens', 'grenades', 'flame-throwers', 'staples']
for i,item in enumerate(supplies, 5):
    print('INDEX=> ' + str(i) + ' in supplies is: ' + item)

# yields=>
# INDEX=> 5 in supplies is: pens
# INDEX=> 6 in supplies is: grenades
# INDEX=> 7 in supplies is: flame-throwers
# INDEX=> 8 in supplies is: staples

