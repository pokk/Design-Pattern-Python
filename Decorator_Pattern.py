""" Created by Jieyi on 1/21/16. """
from abc import abstractmethod, ABCMeta


class Meal(metaclass=ABCMeta):
	"""
	Meal's interface.
	"""
	@abstractmethod
	def price(self):
		...

	@abstractmethod
	def getContent(self):
		...


class FriedChicken(Meal):
	"""
	Main meal: Fried Chicken.
	"""
	def price(self):
		return 49.0

	def getContent(self):
		return 'Fried Chicken'


class Hamburger(Meal):
	"""
	Main meal: Hamburger
	"""
	def price(self):
		return 99.0

	def getContent(self):
		return 'Crab Hamburger'


class SideDish(Meal, metaclass=ABCMeta):
	"""
	Main meal: Side Dish interface.
	"""
	def __init__(self, meal):
		self._meal = meal


class Salad(SideDish):
	"""
	Decorator: Add the some side dish.
	"""
	def __init__(self, meal):
		super(Salad, self).__init__(meal)

	def price(self):
		return self._meal.price() + 10.0

	def getContent(self):
		return self._meal.getContent() + ', Salad'


class Coke(SideDish):
	"""
	Decorator: Add the some side dish.
	"""
	def __init__(self, meal):
		super(Coke, self).__init__(meal)

	def price(self):
		return self._meal.price() + 15.0

	def getContent(self):
		return self._meal.getContent() + ', Coke'


def main():
	meal = FriedChicken()
	print("meal : %s ; price : %f" % (meal.getContent(), meal.price()))
	meal = Salad(meal)
	print("meal : %s ; price : %f" % (meal.getContent(), meal.price()))
	meal = Coke(meal)
	print("meal : %s ; price : %f" % (meal.getContent(), meal.price()))


if __name__ == '__main__':
	main()
