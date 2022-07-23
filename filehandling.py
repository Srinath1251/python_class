# file  = open('groceries.py', 'r')
# data = file.read()

# writing to a new file
new_file = open("items.py", 'w')

name = input('Enter your name')
new_file.write("Hi {}. Welcome to the world of python programming".format(name))

# writing multiple lines
fruits = ('Apple ', 'Mango ', 'Grapes ', 'Oranges ')

new_file.writelines('\n')
new_file.writelines(fruits)
new_file.writelines('\n')

# closing file
new_file.close()

# append
file = open('items.py', 'a')

file.write("This is appending text to an existing file")

file.close()

# read file
read_file = open('items.py', 'r+')
print(read_file.readline())
# print(read_file.read())
print(read_file.readline(20))

# with
# used to perform operations on files without closing the file each time
with open('fruits.txt', 'w') as file:
    file.write('Banana,Apple,Custard Apple,Grapes')

with open('items.py', 'r') as rfile:
    print(rfile.read())

with open('fruits.txt', 'a') as afile:
    afile.write(',Guava,Strawberry,Papaya')

with open('fruits.txt', 'r') as readfile:
    print(readfile.read())
