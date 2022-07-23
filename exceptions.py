import sys

fruits = ['Mango', 'Apple', 'Banana', 'Grapes']

#
print('TYPE-1')
try:
    print(fruits[5])
except:
    errorInfo = sys.exc_info()
    print(errorInfo[0], errorInfo[1])

#
print('TYPE-2')
try:
    print(fr[6])
except IndexError:
    errorInfo = sys.exc_info()
    print(errorInfo[0], errorInfo[1])
except:      # default exception
    print('This is default exception')

#
print('TYPE-3')
try:
    print(fruits[1])
    import testingFile
    print(fr[2])
except IndexError:
    errorInfo = sys.exc_info()
    print(errorInfo[0], errorInfo[1])
except IOError:
    print('This is IO exception error')
except ImportError:
    print('This is import error')
except:     # default exception
    print('This is default exception')
else:       # When no exception ocur, this else part will execute
    print('This is else part')
finally:   # this will execute always irespective of exceptions
    print('This will print anyway')
