# Numeric(int, float, complex)
#---------------------------------------------------------------------#
marks = 536
total = 600
percentage = (marks/total) * 100

print("Percentage is : ", percentage)
print("Type of Marks is :", type(marks))
print("type of percentage is : ", type(percentage))

x = 3 + 5j

print(type(x))
print(x.real)
print(x.imag)

# Sequence type(Strings, List, Tuple)
#--------------------------------------------------------------------#

# Strings : strings are IMMUTABLE
# we cannot change or delete characters in a string instead we can change the entire string.
description = '''   This is description
about Python course.
Happy to learn Python programming
'''
city = 'Ramagundam'
colony = 'NTPC'

print(description)
print("Length of description is : ", len(description))

print(city[2])

print('Checking Python in description:')
print('Python' in description)

#city[1] = J    # this gives error. we cannot change the character in a string

del colony

#print(colony)  # here it is already deleted

# string slicing [start : end : step]
print(city[2:7])
print(city[2:8:2])
print(city[:6])
print(city[4:])
print(city[::-1])   # reverse a string

# LIST
personalInfo = ['Srinath', 'Hyderabad', 33, 'Software Engineer']
fruits = ['Apple', 'Grapes', 'Banana']

#1. ORDERED: list always prints the elements as mentioned in order
print(personalInfo)
print(personalInfo)

#2. NESTED: list can be nested
veg = ['Tomato', 'Cauliflower', 'Brinjal', fruits]
print(veg)

print(len(veg))
print(type(veg))

#3. INDEXING
print(veg[3][1])
print(veg[-2])  # second element from the last

#4. MUTABLE: list elements are mutable
fruits[2] = 'Mango'
print(fruits)
print(fruits * 2)

#5. APPEND: elements can be appended to the list
fruits.append('Watermelon')     # appending a single element
print(fruits)
    
# adding multiple elements can be done this way
fruits.extend(['Guava', 'Custard Apple', 'Pine Apple'])
print(fruits)

fruits.insert(0, 'Kiwi')
print('After inserting Kiwi in the 0 index :', fruits)

fruits[1:1] = ['Papaya', 'Pomegranate', 'Orange']
print(fruits)

# wrong way of appending multiple elements
#fruits.extend('Guava', 'Custard Apple', 'Pine Apple')

#6. Allows DUPLICATE values
veg.append('Tomato')
print(veg)

#7. CONCATENATION
print(veg + fruits)

#8. Deleting/Removing List items
del fruits[1]
print('After deleting index 1 from fruits list: ', fruits)
del fruits[3:7]
print('After deleting elements from index 3 to 7', fruits)
# del fruits    # this will delete the complete list

# removing specific item from list
fruits.remove('Orange')
print('After removing orange from list :', fruits)

# pop:
# pop(index): removes specified index value and returns it
# pop(): removes the last value and returns it
print(fruits.pop(0))
print(fruits.pop())
print(fruits)


# removing duplicate values in a list
nums = [10, 20, 30, 40, 50, 20, 40, 60, 70, 10, 30, 90]
nums = set(nums)
nums = list(nums)
print(nums)



# TUPLE
friends = ('Krishna', 'Shekar', 'Varaprasad', 5.5, 5.9, 5.11, 'Good', 'Better', 'Best')
print(friends)
print(type(friends))

print(friends[2])

hobbies = ('Coding')    # this becomes string.
print(type(hobbies))

hobbies = ('Coding',)   # this is a tuple
print(type(hobbies))

# list can be included in a tuple
# tuple allows duplicate values
hobbies = ('Coding', ['Drawing', 'Painting', 'Running'], 'Coding')
print(type(hobbies))
print(type(hobbies[1]))
print(hobbies[1][1])
hobbies[1][1] = 'Swimming'
print('After changing the list element in the tuple :', hobbies)


# SET
#------------------------------------------------------------#
data = {'Srinath', 'Hyderabad', 5.8, 30}

# unordered. It doesnt follow order. So, we cannot index and slice elements
print(data)

# empty set
players = set()
#players = {}   # this becomes dictionary. not an empty set
print(type(players))


# adding single elelment
data.add('Ramagundam')
print(data)

# adding multiple elements
data.update(['Coding', 'Drawing', 'Cooking', 'Running'])
#data.add(['Coding', 'Drawing', 'Cooking']) # this is wrong way of appending
print(data)

data.add('Coding')  # ignores duplicate values. Coding is already there. So it ignores this
print(data)

# removing an element in a set
data.remove('Cooking')
print('After removing "Cooking" from set :', data)

# discard will not show error even if the element is not found
data.discard('Running')
data.discard('Dancing')
#data.remove('Dancing')     # will throw an error
print(data)

# removing all elements in a set
data.clear()
print(data)


# DICTIONARY
# elements are unordered
personalInfo = {'name': 'Srinath', 'age': 30, 'height': 5.8, 'artist': True}
print(personalInfo)
print(type(personalInfo))


# mutable
personalInfo['name'] = 'Manchikatla'
print(personalInfo)

# duplicate values are allowed but duplicate keys are not allowed
personalInfo = {'name': 'Srinath', 'age': 30, 'height': 5.8, 'nickname': 'Srinath'}
print(personalInfo)
personalInfo = {'name': 'Srinath', 'age': 30, 'height': 5.8, 'name': 'MANCHIKATLA'}
print(personalInfo)

# nested dictionary
skills = {'Coding': 'Python', 'Singing': False, 'Drawing': 'Excellent'}
personalInfo = {'name': 'Srinath', 'age': 30, 'talent': skills}
print(personalInfo)
print(personalInfo['talent']['Drawing'])
