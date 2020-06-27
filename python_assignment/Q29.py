# Write a Python script to concatenate following dictionaries to create a new
# one.

def concatenate_dicts(*args):
    '''

    :param arg: dictionaries
    :return: dictionary
    '''
    new_dict = {}
    for arg in args:
        for key, value in arg.items():
            new_dict[key] = value

    return new_dict


if __name__ == '__main__':
    print(concatenate_dicts({1:10, 2:20}, {3:30, 4:40}, {5:50, 6:60}))