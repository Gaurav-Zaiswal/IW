# Write a Python program to multiply all the items in a dictionary.

def mul_dict(kwarg):
    '''

    :param kwarg: Dictionary
    :return: Number
    '''
    sum = 1
    for value in kwarg.values():
        # print(value)
        sum *= value

    return sum


if __name__ == '__main__':
    print(mul_dict({
        'rice': 50,
        'water': 25,
        'apple': 90,
        'mango': 78
    }))