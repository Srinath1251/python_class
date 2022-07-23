original_sum = 100  # global scope


def calculate_sum():
    global original_sum          # if this is used, global sum gets changed
    new_sum = 200       # local scope
    original_sum = 300
    original_sum += 50
    total = original_sum + new_sum
    print("Total sum is : ", total)


calculate_sum()
#print(newSum)      # newSum belongs to localscope.Hence cannot be accessed
print("Original sum value is : ", original_sum)      # prints global variable value
