# Write a Python program to count the occurrences of each word in a given
# sentence.

def count_occurrences(arg):
    '''

    :param arg: sentence:String
    :return: occurrence of each word:Dictionary
    '''
    word_list = arg.split()
    word_occurrence = {}
    for word in word_list:
        if word in word_occurrence:
            word_occurrence[word] += 1
        else:
            word_occurrence[word] = 1
    return word_occurrence


if __name__ == '__main__':
    print(count_occurrences('a lazy fox jumps over another lazy fox sitting below a tree '
                            'over and over and it jumps over a tree as well'))