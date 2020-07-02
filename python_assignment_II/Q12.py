# Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.
def is_palindrome(word):
    '''

    :param word: string
    :return: boolean
    '''
    return word == word[::-1]

print(is_palindrome('dad'))
print(is_palindrome('mom'))