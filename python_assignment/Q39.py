# Write a Python program to unpack a tuple in several variables.

def tuple_to_list(arg):
    '''

    :arg: tuple
    :return: list
    '''
    return list(arg)

def tuple_to_set(arg):
    '''

    :arg: tuple
    :return: set
    '''
    return set(arg)

def tuple_to_string(arg):
    '''

    :arg: tuple
    :return: string
    '''
    s = ''
    for item in arg:
        s += str(item)
    return s

if __name__ == '__main__':
    t = (2,3,4,5)
    print('given tuple: ', t)
    print('list: ', tuple_to_list(t))
    print('set: ', tuple_to_set(t))
    print('string: ', tuple_to_string(t))