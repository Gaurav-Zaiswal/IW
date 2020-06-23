# Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).

def sort_words(arg):
    '''

    :param arg: word:String
    :return: List:String
    '''
    unique_word_list = list(set(arg))
    unique_word_list.sort()
    for word in unique_word_list:
        if word in arg:
            arg.remove(word)

    for _ in arg:
        unique_word_list.append(_)

    return unique_word_list


if __name__ == '__main__':
    # word_list = input().strip().split(', ')
    temp = sort_words(['red', 'white', 'black', 'red', 'green', 'black'])
    temp = ', '.join(temp)
    print(temp)