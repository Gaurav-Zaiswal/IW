# Write a Python program to slice a tuple.

def slice_tuple(arg):
    '''

    :arg: tuple
    :return: tuple
    '''
    t_l = [arg[x] for x in range(0, len(arg) //2 )]
    return tuple(t_l)


if __name__ == '__main__':
    t = (2,3,4,5)
    print('given tuple: ', t)
    print('Tuple after slicing to half: ', slice_tuple(t))