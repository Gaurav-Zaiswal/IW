# Write a Python program to insert a given string at the beginning of all items in
# a list.

def add_string(*args):
    '''

    :param arg: first:list, second:string
    :return: list
    '''

    for _ in range(len(args[0])):
        args[0][_] = str(args[0][_]) + args[1]
    return args[0]


if __name__ == '__main__':
    print(add_string([1,2,3,4], 'emp'))