from datetime import date

#print(date.today().month)

yearOfBirth = int(input("Enter your Year of birth"))
currentYear = date.today().year

print("Your age in years is : ", currentYear - yearOfBirth)
