# Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.

def count_case(word):
    '''

    :param word: string
    :return: dictionary
    '''
    d = {
        'lower_case': 0,
        'upper_case': 0
    }
    for _ in word:
        if ord(_) in range(97, 123):
            d['lower_case'] += 1
        elif ord(_) in range(65, 91):
            d['upper_case'] += 1
    return d

if __name__ == "__main__":
    print(count_case('The quick Brow Fox'))