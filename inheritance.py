class Class1:
    name = 'Srinath'
    __salary = 35000

    def __init__(self):
        self._company = 'Rize Software Solutions'
        print('(Private) My salary is ', self.__salary)

    @staticmethod
    def method1():
        print('Method 1')
        # print(self.__salary)


class Class2:
    _age = 30

    def __init__(self):
        self.job = 'Software Engineer'

    @staticmethod
    def method2():
        print('Method 2')


class Class3(Class1, Class2):
    def __init__(self):
        Class1.__init__(self)
        Class2.__init__(self)
        print(Class2._age)
        print(Class1.method1())
        # print('Company name is : ', Class1._company)

    @staticmethod
    def method3():
        print('Method 3')


c3 = Class3()
c3.method3()
# c3.method2()

# print(c3.name)
# print(c3._age)
# c2 = Class2()
# print(c2.job)
#print(c3.__salary)     # error
