# ----------------------------------------------------------------------
#
#   list_value_ex.py - a python script showing example of indexing a
#                      list
#
#
# ---------------------    module history   ----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
# ----------------------------------------------------------------------

supplies = ['pens', 'grenades', 'flame-throwers', 'staples']
print(supplies.index('grenades'))


# Loop with index
for i, item in enumerate(supplies):
    print(i, item)
# yields =>
# 0 pens
# 1 grenades
# 2 flame-throwers
# 3 staples


# List comprehension with index
list_comp = [(i, item) for i, item in enumerate(supplies)]
print(list_comp)
# yields =>
# [(0, 'pens'), (1, 'grenades'), (2, 'flame-throwers'), (3, 'staples')]

# --------
# Indexing
# --------
print(supplies[0])
# yields => 'pens'

print(supplies[1])
# yields => 'grenades'

print(supplies[-1])
# yields => 'staples'

print(supplies[-2])
# yields => 'flame-throwers'

# ------------------------------
# Slicing (up to, not including)
# ------------------------------
print(supplies[:2])
# yields => ['pens', 'grenades']

print(supplies[:-1])
# yields => ['pens', 'grenades', 'flame-throwers']

# ----------------
# Every other item
# ----------------
print(supplies[::2])
# yields => ['pens', 'flame-throwers']

# -------
# Reverse
# -------
print(supplies[::-1])
# yields => ['staples', 'flame-throwers', 'grenades', 'pens']

# -------------------------------------------------
# Reverse in place (CATIOIN: mutates original list)
# -------------------------------------------------
supplies.reverse()
print(supplies)
