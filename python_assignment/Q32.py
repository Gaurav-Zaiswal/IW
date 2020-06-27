# Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x) i.e. value is square of key.

def create_dict(number):
    '''

    :param kwarg: number
    :return: dictionary
    '''
    created_dict = {}
    for i in range(1, number+1):
        created_dict[i] = i*i

    return created_dict


if __name__ == '__main__':
    print(create_dict(5))