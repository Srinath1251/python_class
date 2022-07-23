a = 10
num_list = [30, 50, 70]
num_list = a
print(num_list)     # prints 10

a = 10
num_list = [30, 50, 70]
num_list[1] = a
print(num_list)     # prints [30, 10, 70]


def show_list(nums):
    new_list = [5, 10, 15, 20]
    nums = new_list
    return nums


list_num = [1, 2, 3, 4]
print(show_list(list_num))
print(list_num)


def calculate(mrks):
    mrks[1] = 78
    return mrks


marks = [60, 70, 80, 65, 95]
print(calculate(marks))
print(marks)


def change_num(n):
    n = 30
    return n


num = 10
change_num(num)
print(num)


# default parameters
def show_default(val=50):
    print(val)


show_default()
show_default(100)
