# variables
a = 10
fname = 'Srinath'
lname = "Manchikatla"
full_name = "Srinath Manchikatla"
take_home_salary = 35500

# there is no specific keyword for constant in Python. Simply we write in Capital letters.
HEIGHT = 175.6      # this is constant, for our convenience we write like this

print(fname, lname, full_name, sep="->")

print("Height is : ", HEIGHT)

# We can change the constant value also. But dont do this.
HEIGHT = 180.0
print("After changing the constant value, Height is :", HEIGHT)

print(type(HEIGHT))
print(type(take_home_salary))
print(type(full_name))
