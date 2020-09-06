"""
References:
- PEP 484: https://www.python.org/dev/peps/pep-0484/
- Python Type Checking Guide: https://realpython.com/python-type-checking/
- Stat of Type Hints: https://www.bernat.tech/the-state-of-type-hints-in-python/
- Mypy Cheat Sheet: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
"""


def add_ints(x: int, y: int) -> int:
    return x + y


# Since Python will always remain a dynamically type language, all the
# below lines of code will run without error.
print(add_ints(5, 5))
# yields => 10

# This will run without error even though x and y are floats
print(add_ints(5.5, 3.5))
# yields => 9.0

# This will run without error even though x and y are strings
print(add_ints('a', 'b'))
# yields => 'ab'


# Type hints work with Union (more that one type)
from typing import Union


def add_things(
    x: Union[int, float],
    y: Union[int, float]
) -> Union[int, float]:
    return x + y


# Since Python will always remain a dynamically type language, all the
# below lines of code will run without error.
print(add_things(5, 5))
# yields => 10

print(add_things(5.5, 3.5))
# yields => 9.0

# This will run without error even though x and y are strings
print(add_things('a', 'b'))
# yields => 'ab'


# Works for dictionary definitions and function returning nothing
from typing import Dict


def print_dict_key_values(d: Dict[str, int]) -> None:
    for k, v in d.items():
        print(f"Key: {k} Value: {v}")


d = {'first': 1, 'second': 2, 'third': 3}
print_dict_key_values(d)

d_strs = {'first': '1', 'second': '2', 'third': '3'}
print_dict_key_values(d_strs)

# Works on other libraries
import numpy as np


def show_array(a: np.ndarray) -> None:
    print(a)


# Prints array
a = np.array([1, 2, 3])
show_array(a)

# Still prints the list... no error at runtime
list_ = [1, 2, 3]
show_array(list_)


# Can specify an optional parameter
from typing import Optional


def print_if_exists(thing: Optional[Union[str, int, float]] = None) -> None:
    if isinstance(thing, (str, int, float)):
        print("things exists!")
    else:
        print("thing is None")


x = 'a'
print_if_exists(x)
# yields => thing exists!

print_if_exists()
# yields => thins is None
