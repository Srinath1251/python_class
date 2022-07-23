def show_data(name, age, salary):
    print('My name is {}. Age is {} and Salary is {}'.format(name, age, salary))


show_data('Srinath', 30, 45000)

# Variable number of arguments
# *args
# *kwargs


# *args
def show_all(*args):
    for arg in args:
        print(arg)


show_all(10, 20, 30, 40)


def print_info(*args):
    for arg in args:
        print(arg)


print_info('Srinath', 'Software Developer', 'Hyderabad', 30)
print_info('Srinath', ['Software Developer', 'Hyderabad', 30], ('NTPC',))


# product of numbers using *args
def product_of_nums(*args):
    result = 1
    for arg in args:
        result = result * arg
    return result


print(product_of_nums(2, 3, 4, 5, 2))


def multiply_nums(first, *args):
    product = first
    for arg in args:
        product = product * arg
    return product


print(multiply_nums(2, 3, 4, 5))


# We can specify argument name and value together using kwargs
# **kwargs -> variable number of keyword arguments
def bio_data(**kwargs):
    for key, val in kwargs.items():
        print('{} --> {}'.format(key, val))


bio_data(name='Srinath', age=30, job='SWE')


def test_function(course, scope, fees):
    print(course, scope, fees)


test_function(fees=25000, course='PHP', scope=True)
