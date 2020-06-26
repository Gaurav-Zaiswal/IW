# Write a Python program to replace the last element in a list with another list.

def concatenate_lists(*args):
    '''

    :param arg: first:list, second:string
    :return: list
    '''

    for _ in args[1]:
        args[0].append(_)
    return args[0]


if __name__ == '__main__':
    print(concatenate_lists([1,2,3,4], [10,11]))