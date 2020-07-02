# Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

def binary_search(arr, key, index=0):
    '''

    :param arr: list
    :param key: number
    :return: number
    '''
    # print(arr, key)
    length = len(arr)
    if 0 <= length-1:
        mid =  length // 2
        # print('mid index: ',mid)
        mid_item = arr[mid]
        # print('mid item: ',mid_item)
        index += mid

        if mid_item == key:
            return index

        elif key < mid_item:
            left_arr = arr[:mid]
            # print('left child: ',left_arr)
            return binary_search(left_arr, key, index - mid)

        else:
            right_arr = arr[mid+1:]
            # print('right child: ', right_arr)
            return binary_search(right_arr, key, index + 1)

    return -1


arr = [1,2,3,4,5,6,7,8,9]
key = 6
print(binary_search(arr, key))
