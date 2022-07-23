# simple if statement if there is only one statement to be printed
rank = 100
if rank == 100:
    print('You have secured a good rank')

rank = 75
if rank > 50:
    print('Your rank is greater than 50.')
    print('Congrats')
    if rank < 100:
        print('Also your rank is less than 100')
        print('Again congrats!!!')

# if else condition
coins = 20
if coins == 20:
    print('There are 20 coins')
else:
    print('Sorry coins are not 20 in number')

# if else shorthand
a = 10
print('Greater than 5') if a > 5 else print('Less than 5')

# if ..elif
'''age = int(input('Enter your age'))
if age >= 18 and age <= 30:
    print('You are an Adult')
elif age >= 13 and age <=17:
    print('You are a teenager')
elif age < 13:
    print('You are a boy')
else:
    print('You are a Matured Old Man')'''


# for loop
marks = [56, 35, 75, 25, 86]    # list
for item in marks:
    print(item)

fruits = ('Mango', 'Apple', 'Orange', 'Pineapple', 'Banana', 'Mango')   # tuple
for fruit in fruits:
    print(fruit)

personalInfo = {'name': 'Srinath', 'age': 30, 'height': 5.8, 'nickname': 'Srinath', 'name': 'Srinath Manchikatla'}
for key in personalInfo:
    print(personalInfo[key])

name = "Sri"
for character in name:
    print(character)

# prints item from 0 to 4
print('Printing from 0 to 4 using range')
for item in range(5):
    print(item)

print('Printing from 1 to 5 using range')
for item in range(1, 6):
    print(item)

print('Printing from 5 to 1 in decending order using range')
for item in range(5, 0, -1):
    print(item)

# extracting last 2 chars in a string and printing in pattern
name = input('Enter your name (to extract last 2 chars and print in a pattern)')
last_two_chars = name[-2:]

for item in range(1, 11):
    print(last_two_chars*item)

# extracting vowels and consonents in a string
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_list = []
consonents_list = []

name = input('Enter your name (to extract vowels and consonents)')

for character in name:
    if character != ' ':
        if character in vowels:
            vowels_list.append(character)
        else:
            consonents_list.append(character)
        #vowel_list.append(character) if character in vowels else consonents_list.append(character)

print(vowels_list)
print(consonents_list)
