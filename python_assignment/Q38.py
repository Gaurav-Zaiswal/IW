# Write a Python program to remove a key from a dictionary.

def remove_dict_key(*args):
    '''

    :args: dictionary followed by key
    :return: dictionary
    '''
    sum = 1
    del args[0][args[1]]

    return args[0]


if __name__ == '__main__':
    print(remove_dict_key(
        {
            1:2,
            2:3,
            3:4
        }, 1
    ))