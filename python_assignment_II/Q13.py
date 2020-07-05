# Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple.

import csv

def export_to_csv(file_name, args) -> None:
    '''

    :param file_name: String -> file name without extension
    :param args: list -> list of tuples, tuples has name, address, and age in it consecutively
    :return: None
    '''
    result_file_name = file_name + '.csv'
    with open(result_file_name, mode='w') as employee_file:
        fieldnames = ['Name', 'Address', 'Age']
        employee_writer = csv.DictWriter(employee_file, fieldnames=fieldnames)

        employee_writer.writeheader()
        for arg in args:
            employee_writer.writerow({'Name': arg[0],
                                      'Address': arg[1],
                                      'Age': arg[2]
                                      })

# calling the function
export_to_csv('my_friends_info', [('abc', 'asdfd', 23),
                                  ('mohan', 'ramechap', 90),
                                  ('mahadev', 'himalayas', 1)])
