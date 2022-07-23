data = {1: 'Srinath', 2: 'Lalith', 3: 'Madhu'}

# break
print('Using break:')
for item in data:
    print(item)
    break
    print('End of printing')

# continue
print('Using continue:')
for item in data:
    print(data[item])
    continue
    print('End of printing')

# Print sum of all the list elements
marks = [60, 75, 83, 92, 77, 86]
sum_of_marks = 0

for item in marks:
    sum_of_marks += item

print("Total marks: ", sum_of_marks)

# Using while loop to print
i = 5
while i < 10:
    print(i)
    i = i + 1

# pass : acts as placeholder
for i in range(10):
    pass
