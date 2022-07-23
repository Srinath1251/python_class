from functools import reduce

# filter function takes the function and iterable and produces the desired results
numbers = [20, 25, 45, 56, 78]


def check_even(num):
    return num % 2 == 0


check = filter(check_even, numbers)
print(list(check))

# filter using lambda function
check = filter(lambda num: num % 2 == 0, numbers)
print(list(check))

# map : takes function and iterable, performs some operation and produces the new results
# it doesnt reduces the actual list of elements
fruits = ['mango', 'banana', 'grapes', 'apple']

capitalize = map(lambda item: item.upper(), fruits)
print(list(capitalize))

# reduce(function, sequence, initial): returns a single result
# In Python 3, to use reduce, you need to import reduce
# from functools import reduce (Write this at the top of file)


nums = [10, 20, 30, 40, 50, 60]

reduce_results = reduce(lambda a, b: a+b, nums, 10)
print(reduce_results)
