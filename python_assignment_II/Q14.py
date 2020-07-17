# Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.

import csv

def read_csv_dict(file_name):
    '''

    :param file_name: String -> file name without extension
    :return: List -> list of dictionary
    '''
    input_file_name = file_name + '.csv'
    with open(input_file_name, mode='r') as csv_file:
        dict_list = []
        csv_reader = csv.DictReader(csv_file)
        # print(csv_reader)
        line_count = 0
        for row in csv_reader:
            # print(row)
            # first line of csv_reader has headers so poping it up
            if line_count == 0:
                line_count += 1
            dict_list.append(row)
            line_count += 1

    return dict_list


# calling function
result = read_csv_dict('my_friends_info')
print(result)
