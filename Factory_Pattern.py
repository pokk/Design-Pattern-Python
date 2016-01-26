""" Created by Jieyi on 1/26/16. """
from abc import ABCMeta, abstractmethod


class IBeverageProvider(metaclass=ABCMeta):
	"""
	The material of the tea (Interface).
	"""

	@abstractmethod
	def AddMaterial(self):
		...

	@abstractmethod
	def Brew(self):
		...

	@abstractmethod
	def PouredCup(self):
		...


class GreenTea(IBeverageProvider):
	def PouredCup(self):
		print('poured green tea to the cup')
		pass

	def AddMaterial(self):
		print('add the green tea')
		pass

	def Brew(self):
		print('brew the hot water into green tea cup')
		pass


class BlackTea(IBeverageProvider):
	def PouredCup(self):
		print('poured black tea to the cup')
		pass

	def AddMaterial(self):
		print('add the black tea')
		pass

	def Brew(self):
		print('brew the hot water into black tea cup')
		pass


class MilkTea(IBeverageProvider):
	def PouredCup(self):
		print('poured milk tea to the cup')
		pass

	def AddMaterial(self):
		print('add the milk tea')
		pass

	def Brew(self):
		print('brew the hot water into milk tea cup')
		pass


class IFactory(metaclass=ABCMeta):
	@abstractmethod
	def CreateBerverage(self):
		...


class GreenTeaFactory(IFactory):
	def CreateBerverage(self):
		return GreenTea()


class BlackTeaFactory(IFactory):
	def CreateBerverage(self):
		return BlackTea()


class MilkTeaFactory(IFactory):
	def CreateBerverage(self):
		return MilkTea()


class BeverageStore:
	def __init__(self, factory):
		self.__factory = factory

	def OrderBeverage(self):
		self.beverage = self.__factory.CreateBerverage()

		self.beverage.AddMaterial()
		self.beverage.Brew()
		self.beverage.PouredCup()


def main():
	store = BeverageStore(MilkTeaFactory())
	store.OrderBeverage()
	
	store = BeverageStore(GreenTeaFactory())
	store.OrderBeverage()


if __name__ == '__main__':
	main()
