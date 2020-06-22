# replace the all the occurences of the first character of a given string with $.
# Note that first character itself should not be changed.

def replace_occurence(original_word):
        first_char = original_word[0]
        return first_char + original_word[1:].replace(first_char, '$')


if __name__ == "__main__":
    print(replace_occurence('restart'))
    print(replace_occurence('oliliyooli'))
