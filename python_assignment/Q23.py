# Write a Python program to check a list is empty or not.

def isEmptyList(arg):
    '''

    :param arg: list of numbers
    :return: Boolean
    '''
    return len(arg)==0


if __name__ == '__main__':
    print(isEmptyList([2, 1, 8 ,4, 8, 3, 2, 1, 5, 4]))