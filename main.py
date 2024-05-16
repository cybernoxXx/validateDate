import datetime

def isValidDate(year, month, day):
    # First i want to check if the year is leap or not
    isLeap = False
    # Check if year is not divisible by 4
    if year % 4 != 0:
        isLeap = False
    # Check if year is not divisible by 100, if is not divisible by 4 and 100 is a leap year
    elif year % 100 != 0:
        isLeap = True
    # Check if year is not divisible by 400, is in not divisible by 4 and 400 but it's divisible by 100 is a leap year
    elif year % 400 != 0:
        isLeap = False
    # Return true in all the other cases
    else:
        isLeap = True

    # Second i want to check which month is, according to the month i can check the day
    isThirty = False
    isThirtyOne = False
    isFebraury = False

    if month in [4, 6, 11]:
        isThirty = True
    elif month in [1, 3, 5, 7, 8, 9, 10, 12]:
        isThirtyOne = True
    elif month == 2:
        isFebraury = True
    else:
        return False

    if day in range(1,31) and isThirty == True:
        return True
    elif day in range(1,32) and isThirtyOne == True:
        return True
    elif day in range(1,29) and isFebraury == True and isLeap == False:
        return True
    elif day in range(1, 30) and isFebraury == True and isLeap == True:
        return True

    return False



assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False

d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)

for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True

    d += oneDay
