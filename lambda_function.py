# lambda is nothing but an anonymous function which returns a single  statement

res = lambda num: 2 * num
print(res(2))

# another way
res = (lambda num: 2 * num)(3)
print(res)

res = lambda num: num*num*num
print(res(3))
