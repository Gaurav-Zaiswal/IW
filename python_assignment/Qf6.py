# Write a Python function to check whether a number is in a given range.

def is_in_range(*args):
    '''

    :param arg: number, list of numbers(range)
    :return: boolean
    '''
    args[1].sort()
    return args[0] >= args[1][0] and args[0] <= args[1][1]

if __name__ == "__main__":
    print(is_in_range(-5, [-20, -10]))
    print(is_in_range(5, [0, 10]))