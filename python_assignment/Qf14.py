# Write a Python program to sort a list of dictionaries using Lambda.

sort_dict = lambda arg: arg['roll']


if __name__ == '__main__':
    l = [
        {'roll': 10},
        {'roll': 5},
        {'roll': 8},
        {'roll': 1},
        {'roll': 4},
        {'roll': 3},

    ]
    l.sort(key=sort_dict)
    print(l)