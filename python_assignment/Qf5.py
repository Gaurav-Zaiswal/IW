# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.

def cal_fact(arg):
    '''

    :param arg: number
    :return: number
    '''
    if arg >= 0 and type(arg) is int:
        if arg in [0, 1]:
            return 1
        elif arg == 2:
            return 2
        else:
            return arg * cal_fact(arg-1)
    else:
        return 'non negative integer is required'

if __name__ == "__main__":
    print(cal_fact(5))