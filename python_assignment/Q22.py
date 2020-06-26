# Write a Python program to remove duplicates from a list.

def remove_duplicates_from_list(arg):
    '''

    :param arg: list of numbers
    :return: arg:list
    '''
    return list(set(arg))


if __name__ == '__main__':
    print(remove_duplicates_from_list([2, 1, 8 ,4, 8, 3, 2, 1, 5, 4]))