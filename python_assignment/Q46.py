# Write a Python program to find the length of a tuple

def tuple_length(arg):
    '''

    :arg: tuple
    :return: number
    '''
    return len(arg)


if __name__ == '__main__':
    t = (2,3,4,5)
    print('given tuple: ', t)
    print('legth: ', tuple_length(t))