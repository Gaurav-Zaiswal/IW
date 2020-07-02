# Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.

def change_case(camel_case=None, kebab_case=None):
    if camel_case:
        snake_case = ''
        snake_case += camel_case[0].lower()
        for _ in camel_case[1:]:
            if ord(_) in range(65, 91):
                snake_case += '_'
            snake_case += _
        return snake_case.lower()

    if kebab_case:
        return kebab_case.replace("-", "_")


print('ThisIsNepal: ', change_case(camel_case="ThisIsNepal"))
print('this-is-nepal: ', change_case(kebab_case="this-is-nepal"))
