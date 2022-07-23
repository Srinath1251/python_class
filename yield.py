# Generator function: it contains yield in it. Returns the generator object
# yield : it stops the function execution and send the result to the
# caller and them resumes back where it left
def calculate_total(items):
    total = 200 * items
    yield total
    print("This is print after yield")


# this returns generator object
# here total_amount is a generator object
total_amount = calculate_total(10)

for i in total_amount:
    print('Total Amount is :')
    print(i)
