# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

def make_unique_list(arg):
    '''

    :param arg: string
    :return: list
    '''
    return list(set(arg))

if __name__ == "__main__":
    print(make_unique_list([1,2,3,3,3,3,4,5]))