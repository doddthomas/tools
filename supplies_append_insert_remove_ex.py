#-----------------------------------------------------------------------
#
#   supplies_append_insert_remove_ex.py - a python script showing list
#                                         example of append/remove/sort
#           
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------
 
 
supplies = ['pens', 'grenades', 'flame-throwers', 'staples']
supplies.append('moose')
print(supplies)
#yields =>  ['pens', 'grenades', 'flame-throwers', 'staples', 'moose']
 
supplies.insert(2,'inserted_2_value')
print(supplies)
#yields => ['pens', 'grenades', 'inserted_2_value', 'flame-throwers', 'staples', 'moose']
 
supplies.remove('inserted_2_value')
print(supplies)
 
supplies.sort()
print(supplies)
#yields => ['flame-throwers', 'grenades', 'moose', 'pens', 'staples']
 
spam=['a','z','Z','A']
spam.sort()
print(spam)
 
spam.sort(key=str.lower)
print(spam)
 
