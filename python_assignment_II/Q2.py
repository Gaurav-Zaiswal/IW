# Write an if statement to determine whether a variable holding a year
# is a leap year.

def is_a_leap_year(year):
    '''
    return True if year is leap, False otherwiae

    :param year: number
    :return: boolean
    '''
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    return False

if __name__ == '__main__':
    print(is_a_leap_year(2020))
    print(is_a_leap_year(2019))
