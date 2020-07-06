# Write a Python class to find the three elements that sum to zero
# from a list of n real numbers.

def find_sublists(arr):
    list_of_sub_lists = []
    for i in range(len(arr)):
        sub_list = []
        for j in range(i+1, len(arr)-i-1):
            sum_of_two_elements = arr[i] + arr[j]
            if -sum_of_two_elements in arr and -sum_of_two_elements not in sub_list:
                sub_list.append(arr[i])
                sub_list.append(arr[j])
                sub_list.append(-sum_of_two_elements)
                list_of_sub_lists.append(sub_list)

    return list_of_sub_lists


print(find_sublists([-25, -10, -7, -3, 2, 4, 8, 10]))
