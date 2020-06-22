# write a program to count the frequency of characters in the string

def count_characters(word):
    '''

    :param word: any String
    :return: dictionary
    '''
    character_frequency = {}
    for w in word:
        if not w in character_frequency:
            character_frequency[w] = 1
        else:
            character_frequency[w] += 1

    return character_frequency



if __name__ == "__main__":
    print(count_characters('gaurav_jaiswal'))
