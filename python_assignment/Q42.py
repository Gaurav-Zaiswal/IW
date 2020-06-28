# Write a Python program to convert a list to a tuple.

def list_to_tuple(arg):
    '''

    :arg: list
    :return: tuple
    '''
    return tuple(arg)

if __name__ == '__main__':
    t = [2,3,4,5]
    print('list: ', t)
    print('tuple: ', list_to_tuple(t))