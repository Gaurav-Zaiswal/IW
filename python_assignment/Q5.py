# Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.

def add_ing(word):
    '''

    :param word: String
    :return: String
    '''

    if len(word)>=3 and word[-3:] != 'ing':
        return word+'ing'
    elif len(word) >= 3 and word[-3:] == 'ing':
        return word + 'ly'
    return word


if __name__ == "__main__":
    print(add_ing('django'))
    print(add_ing('string'))
    print(add_ing('py'))