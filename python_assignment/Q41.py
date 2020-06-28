# Write a Python program to convert a tuple to a string.

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
    print('tupe: ', t)
    print('string: ', tuple_to_string(t))