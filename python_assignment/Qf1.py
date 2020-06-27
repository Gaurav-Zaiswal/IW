# Write a Python function to find the Max of three numbers.

def find_max(*args):
    '''

    :param args: Dictionary
    :return: Number
    '''
    if len(args) != 3:
        return 'Length must be 3'
    if args[0] >= args[1] and args[0] >= args[2]:
        return args[0]
    elif args[1] >= args[0] and args[1] > args[2]:
        return args[1]
    return args[2]


if __name__ == '__main__':
    print(find_max(4,2,9,6))