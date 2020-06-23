# Write a Python program to sum all the items in a list.

def sum_of_items(arg):
    '''

    :param arg: list of numbers
    :return: sum:number
    '''
    sum =0
    for _ in arg:
        sum += _
    return sum


if __name__ == '__main__':
    print(sum_of_items([2, 4, 5, 6,7 ,8]))