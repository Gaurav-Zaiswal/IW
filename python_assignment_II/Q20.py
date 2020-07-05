# Write a Python class to find the three elements that sum to zero
# from a list of n real numbers.

def find_sublists(arr):
    list_of_sub_lists = []
    for i in range(len(arr)-1):
        sub_list = []
        sum_of_two_elements = arr[i] + arr[i+1]
        if -sum_of_two_elements in arr:
            sub_list.append(arr[i])
            sub_list.append(arr[i+1])
            sub_list.append(-sum_of_two_elements)
            list_of_sub_lists.append(sub_list)

    return list_of_sub_lists


print(find_sublists([-25, -10, -7, -3, 2, 4, 8, 10]))
