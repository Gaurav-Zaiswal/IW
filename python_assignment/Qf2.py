# Write a Python function to sum all the numbers in a list.

def find_sum(args):
    '''

    :param args: list
    :return: Number
    '''
    sum = 0
    for _ in args:
        sum += _
    return sum


if __name__ == '__main__':
    print(find_sum([4,2,9,6]))