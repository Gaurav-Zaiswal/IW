# Write a Python function to multiply all the numbers in a list.

def find_sum(*args):
    '''

    :param args: list
    :return: Number
    '''
    sum = 1
    for _ in args:
        sum *= _
    return sum


if __name__ == '__main__':
    print(find_sum(8, 2, 3, -1, 7))