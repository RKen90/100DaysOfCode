'''
DOCSTRINGS

Documentation for the functions that we write

def is_leap_year(year):
    """Takes a year and tells us if that year is a Leap Year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
            
    else:
        return False
'''

def is_leap_year(year):
    """Takes a year and tells us if that year is a Leap Year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
            
    else:
        return False
    
is_leap_year()