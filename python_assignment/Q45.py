# Write a Python program to find the index of an item of a tuple.

def index_of_item(tup, item):
    '''

    :tup: tuple
    :item: element of tup
    :return: tuple
    '''
    return tup.index(item)

if __name__ == '__main__':
    t = (2,3,4,5)
    print('tuple: ', t)
    print('to get the index of: ', 4)
    print('result: ', index_of_item(t, 4))