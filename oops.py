# Class : blueprint to create objects
# Object : it is anything that has state and behavior

class Bottle:
    """This class is used to create Bottle object"""
    # properties / state / static / class variables
    model = 'Kinley'
    price = 2500000
    __formula = 'German'

    def __init__(self, color, capacity):
        # instance variables
        self.color = color
        self.capacity = capacity
        self._engine = 'GFT'    # protected
        self.__technology = 'BZS-X'    # private
        print('################# Parent Constructor #####################')
        self.print_all()

    def __del__(self):
        print('This is parent class destructor')

    # methods/behavior
    def fill_water(self):
        print(self)
        print('Fill water')

    def set_cap(self):
        print(self)
        print('Set cap')

    def wash(self):
        print(self)
        print('(Protected)Engine model is :', self._engine)
        print('(Private)Technology used is :', self.__technology)
        print('Washing bottle')

    def print_all(self):
        print('Engine : ' + self._engine +
            'Technology : ' + self.__technology +
            #'Capacity : ' + self.capacity +
            'Color : ' + self.color +
            #'Price : ' + self.price +
            'Model : ' + self.model +
            'Formula : ' + self.__formula)


print(Bottle.model)
print(Bottle.price)
#print(Bottle.__formula)

bottle1 = Bottle("Silver", 2)       # here silver, 2 are called arguments

print(bottle1.model)
print(bottle1.__doc__)
print(bottle1.capacity)

bottle1.set_cap()


#  INHERITANCE
class SteelBottle(Bottle):
    def __init__(self):
        # Accessing parent class properties/ methods
        # Bottle.__init__(self, 'silver', 3)
        super().__init__('silver', 4)
        self.child_attr = Bottle.price
        print('################## Child constructor ###################')
        print(self.child_attr)

    def __del__(self):
        print('child class destructor')

    def fill_bottle(self):
        print('accessing protected variable of parent class :', self._engine)
        #print('accessing Private variable of parent class :', self.__technology)    # Error
        print('Child class fill bottle method')

    def set_cap(self):
        print('Self cap method from child class')


steel = SteelBottle()
steel.wash()    # calling parent class method
steel.fill_bottle()
steel.set_cap()

# to know the parent class name
print(Bottle.__bases__)
print(SteelBottle.__bases__)


class Car:
    def __init__(self):
        print('This is constructor...')

    def moves_fast(self):
        print('Moves fast.....')

    def makes_sound(self):
        print('Makes sound .....')


c = Car()
c.moves_fast()
c.makes_sound()


class Hyundai(Car):
    pass


h = Hyundai()
