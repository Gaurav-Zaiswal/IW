# Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys

def create_dict():
    '''

    :param kwarg: number
    :return: dictionary
    '''
    created_dict = {}
    for i in range(1, 15):
        created_dict[i] = i*i

    return created_dict


if __name__ == '__main__':
    print(create_dict())