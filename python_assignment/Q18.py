# Write a Python program to get the largest number from a list.

def largest_item(arg):
    '''

    :param arg: list of numbers: list
    :return: largest number:number
    '''
    current_largest = arg[0]
    for a in arg:
        if a > current_largest:
            current_largest = a
    return current_largest


if __name__ == '__main__':
    print(largest_item([2, 4, 5, 16, 7 , 8]))