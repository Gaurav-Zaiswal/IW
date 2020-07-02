# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

def sort_poeple(arr, key):
      '''

      :param arr: list of tuples
      :param key: sorting key
      :return: sorted list
      '''
      if key == 3:
            # sort by age
            new_arr = sorted(arr, key= lambda people: people[2])
            return new_arr

      if key == 2:
            # sort by last name
            new_arr = sorted(arr, key= lambda people: people[1])
            return new_arr

      if key == 1:
            # sort by last name
            new_arr = sorted(arr, key= lambda people: people[0])
            return new_arr

people = []

my_info = ('Gaurav', 'Jaiswal', 22)
people.append(my_info)
my_info1 = ('Saurav', 'Pun', 24)
people.append(my_info1)
my_info2 = ('Ram', 'Poudel', 56)
people.append(my_info2)
my_info3 = ('Shyam', 'Joshi', 2)
people.append(my_info3)
my_info4 = ('Hari', 'Doe', 10)
people.append(my_info4)

print('List of infos: \n', people)
param = None
while not param in [1, 2, 3]:
      param = int(input('\nChoose any sorting parameter\n'
            '1. First Name\n'
            '2. Last Name\n'
            '3. Age\n'))

print('Sorted result: \n',sort_poeple(people, param))


