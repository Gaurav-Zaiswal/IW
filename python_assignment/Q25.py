# Write a Python program to check whether all dictionaries in a list are empty or
# not.

def has_all_empty_dict(args):
    '''

    :param args: list of dictionary
    :return: Boolean
    '''

    flag = 0 # assume true by default
    for arg in args:
        if type(arg) is dict:
            # print(len(arg.items()))
            if len(arg.items()) != 0:
                flag = 1
                break
        else:
            if len(arg) != 0:
                flag = 1
                break
    return flag == 0


if __name__ == '__main__':
    print(has_all_empty_dict([{1:2},{},{}]))
    print(has_all_empty_dict([{},{"name": 'ram'},{}]))
    print(has_all_empty_dict([{},{},{1}]))
    print(has_all_empty_dict([{},{},{}]))