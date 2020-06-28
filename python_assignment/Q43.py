# Write a Python program to remove an item from a tuple.

def remove_item_from_tuple(tup, item):
    '''

    :tup: tuple
    :item: element of tup
    :return: tuple
    '''
    temp = list(tup)
    temp.remove(item)
    return tuple(temp)

if __name__ == '__main__':
    t = (2,3,4,5)
    print('tuple: ', t)
    print('to remove: ', 4)
    print('result: ', remove_item_from_tuple(t, 4))