# Write a Python program to sum all the items in a dictionary.

def sum_dicts(kwarg):
    '''

    :param kwarg: Dictionary
    :return: Number
    '''
    sum = 0
    for value in kwarg.values():
        # print(value)
        sum += value

    return sum


if __name__ == '__main__':
    print(sum_dicts(
        {
            'rice': 50,
            'water': 25,
            'apple': 90,
            'mango': 78
        }
    ))