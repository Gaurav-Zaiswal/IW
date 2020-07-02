# Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.

people = []

# populating people list
my_info = ('Gaurav', 'Jaiswal', 22)
people.append(my_info)
my_info1 = ('Saurav', 'Pun', None)
people.append(my_info1)
my_info2 = ('Ram', 'Poudel', None)
people.append(my_info2)
my_info3 = ('Shyam', 'Joshi', 2)
people.append(my_info3)
my_info4 = ('Hari', 'Doe', 10)
people.append(my_info4)

print('List of people: \n', people)
# to calculate average age
age_sum = 0
for _ in people:
    if not _[2] == None:
        age_sum += _[2]

avg_age = age_sum / len(people)
print('Average age of people: ', avg_age)

# to print older-elder
for _ in people:
    if _[2] is not None and _[2] > avg_age:
        print('{} old'.format(_[0]))

    elif _[2] is not None and _[2] < avg_age:
        print('{} young'.format(_[0]))