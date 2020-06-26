# Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high][1]

    for j in range(low, high):
        if arr[j][1] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


if __name__ == "__main__":
    arr = [(2, 5), (2, 1), (4, 4), (2, 3), (1, 1)]
    arr_length = len(arr)
    quickSort(arr, 0, arr_length-1)
    print(arr)
