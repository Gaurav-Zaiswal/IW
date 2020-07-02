# Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

def binary_search(arr, key):
    '''

    :param arr: list
    :param key: number
    :return: number
    '''
    print(arr, key)
    length = len(arr)
    if 0 < length-1:
        mid =  length // 2
        # print('mid index: ',mid)
        mid_item = arr[mid]
        print('mid item: ',mid_item)

        if mid_item == key:
            return mid

        elif key < mid_item:
            left_arr = arr[:mid]
            # print('left child: ',left_arr)
            binary_search(left_arr, key)

        elif key > mid_item:
            right_arr = arr[mid+1:]
            # print('right child: ', right_arr)
            binary_search(right_arr, key)


    return '-1'

arr = [1,2,3,4,5,6,7,8,9]
key = 7
print(binary_search(arr, key))
