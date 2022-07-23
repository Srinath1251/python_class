# input considers as string irrespective of the type of the entered text
cash = input("Enter the amount you want to withdraw")
cash = int(cash)
print(type(cash))
totalCash = 4500
print("Take your cash : ", cash)
print("Remaining cash is : ", totalCash - cash)

# format the string
print("Take your cash {}, Remaining cash is {} ".format(cash, totalCash - cash))
