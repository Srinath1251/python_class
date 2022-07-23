def even_or_odd(num):
    """This is DOCSTRING. Program to find even or odd"""
    if num % 2 == 0:
        print('{} is even'.format(num))
    else:
        print('{} is odd'.format(num))


even_or_odd(20)
print(even_or_odd.__doc__)
print(print.__doc__)
