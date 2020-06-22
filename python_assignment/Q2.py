# create a word which is made up of first and last two characters of a given string

def create_word(original_word):
    if len(original_word)<2:
        return ''
    else:
        new_word = original_word[:2] + original_word[-2:]
        return new_word


if __name__ == "__main__":
    print(create_word('Python'))
    print(create_word('Py'))