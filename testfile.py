# import extra
print(__name__)

# this function can be imported in another python file
def main():
    print('Hi...This is main function')

print(__name__)

# this code is executed only when it is run seperately
if __name__ == '__main__':
    main()
