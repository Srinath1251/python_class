string = 'Srinath,m,'

# split function splits the string into list
print(string.split(','))
print(string)
print(type(string))

st = string.split(',')
print(st)
print(type(st))

# join function joins the list into string
res = '#'.join('123')
print(res)
print(type(res))

j = '#'.join(st)
print(j)
print(type(j))
