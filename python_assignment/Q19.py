# Write a Python program to get the smallest number from a list.

def smallest_item(arg):
    '''

    :param arg: list of numbers: list
    :return: smallest number:number
    '''
    current_smallest = arg[0]
    for a in arg:
        if a < current_smallest:
            current_smallest = a
    return current_smallest


if __name__ == '__main__':
    print(smallest_item([2, 4, 5, 1, 7 , 8]))