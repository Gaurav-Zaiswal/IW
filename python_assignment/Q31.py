# Write a Python program to iterate over dictionaries using for loops.

def iterate_dicts(kwarg) -> None:
    '''

    :param kwarg: Dictionary
    :return: None
    '''
    for key, value in kwarg.items():
        print(key, value)


if __name__ == '__main__':
    iterate_dicts({1:10, 2:20})