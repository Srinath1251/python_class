def test_func(val):
	val2 = val
	return val2


x = 10
print(test_func(x))

print(x)

# list comprehensions
odd_num_list = [x for x in range(50) if x % 2 != 0]
print(odd_num_list)


def change_index(nums):
	nums[1] = 3


num_list = [1, 2, 3, 4, 5, 6]

change_index(num_list)
print(num_list)


def check_reference(nums):
	nums = [10, 20, 30]
	return nums


num_list = [1, 2, 3, 4, 5, 6]

check_reference(num_list)
print(num_list)
# print(nums) 			# this gives error as nums is local to function


class Car:
	_engine = 'German Technology'		 # protected
	__luxury = True			# private
	wheels = 4			# public

	def __init__(self):
		self.safety_rating = 4
		print('This is parent constructor')

	def moves_fast(self, kmph):
		print(f'car moves with a speed of {kmph} km/hr')
		print(f'This is made with {self._engine}')
		if self.__luxury:
			print('This is luxury car')
		print(f'safety car with rating {self.safety_rating}')


class FordCar(Car):
	def __init__(self, name, price):
		print('This is child class constructor')
		self.safety_rating = 3
		# to use parent constructor
		super().__init__()
		print(f'Car name is {name} and price is {price}')
		print(f'Car rating is : {self.safety_rating}')

	def __del__(self):
		print('This is destructor')


obj = Car()
print(obj.wheels)
# print(obj._engine)			# this is protected
# print(obj.__luxury)			# this is private

obj.moves_fast(20)

ford = FordCar('Ford', '900000')
