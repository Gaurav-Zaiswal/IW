# Write a Python program to find if a given string starts with a given character
# using Lambda.

has_given_first_char = lambda word, char: word[0] == char


if __name__ == '__main__':
    print(has_given_first_char('gaurav', 'g'))