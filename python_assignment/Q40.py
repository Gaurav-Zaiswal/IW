# Write a Python program to add an item in a tuple.

def add_to_tuple(tup, item):
    '''

    :param tup: tuple
    :param item: item to be added
    :return: tuple
    '''
    t = list(tup)
    t.append(item)
    return tuple(t)


if __name__ == '__main__':
    t= 2,3,4,5
    print('given tuple: ', t)
    print('new item has been added: ', add_to_tuple(t, 0))