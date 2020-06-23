# Write a Python program to multiplies all the items in a list.

def multiplication_of_items(arg):
    '''

    :param arg: list of numbers
    :return: sum:number
    '''
    multiply =1
    for _ in arg:
        multiply *= _
    return multiply


if __name__ == '__main__':
    print(multiplication_of_items([2, 4, 5, 6,7 ,8]))