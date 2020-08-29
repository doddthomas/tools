#-----------------------------------------------------------------------
#
#   exception_ex.py - a python script showing example of trapping and
#                     handling a divide by zero exception error
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------


def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('ERROR: invalid argument')


print(spam(2))
# yields => 21.0

print(spam(12))
# yields => 3.5

print(spam(0))
# yields => ERROR: invalid argument
#           None

print(spam(1))
# yields => 42.0


# Example of Traceback
42 / 0

# yields =>

# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# <ipython-input-11-892840ca7299> in <module>
# ----> 1 42/0

# ZeroDivisionError: division by zero


# Can print the message of the error by capturing the error
def spam_message_only(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError as e:
        print(e)


print(spam_message_only(0))
# yields => division by zero
#           None


# Can capture ANY exception and print class and message
def spam_name_message(divide_by):
    try:
        return 42 / divide_by
    except Exception as e:
        print(e.__class__.__name__, e)


print(spam_name_message(0))
# yields => ZeroDivisionError division by zero
#           None


# Can create custom exception
class FavoriteNumberError(Exception):
    # Save the divide_by number used
    def __init__(self, number):
        self.number = number

    # Define an error message
    def __str__(self):
        return f'{self.number} is my favorite number and cannot be used here!'


def spam_custom(divide_by):
    try:
        if divide_by == 5:
            raise FavoriteNumberError(5)
        return 42 / divide_by
    except (ZeroDivisionError, FavoriteNumberError) as e:
        print(e)


print(spam_custom(0))
# yields => division by zero
#           None

print(spam_custom(5))
# yields => 5 is my favorite number and cannot be used here!
#           None

