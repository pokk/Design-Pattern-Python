""" Created by Jieyi on 1/26/16. """
from abc import ABCMeta, abstractmethod


class IBeverageProvider(metaclass=ABCMeta):
    """
    The material of the tea (Interface).
    """

    @abstractmethod
    def add_material(self):
        pass

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def poured_cup(self):
        pass


# Product
class GreenTea(IBeverageProvider):
    def poured_cup(self):
        print('poured green tea to the cup')
        pass

    def add_material(self):
        print('add the green tea')
        pass

    def brew(self):
        print('brew the hot water into green tea cup')
        pass


class BlackTea(IBeverageProvider):
    def poured_cup(self):
        print('poured black tea to the cup')
        pass

    def add_material(self):
        print('add the black tea')
        pass

    def brew(self):
        print('brew the hot water into black tea cup')
        pass


class MilkTea(IBeverageProvider):
    def poured_cup(self):
        print('poured milk tea to the cup')
        pass

    def add_material(self):
        print('add the milk tea')
        pass

    def brew(self):
        print('brew the hot water into milk tea cup')
        pass


# Factory
class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_beverage(self):
        pass


class GreenTeaFactory(IFactory):
    def create_beverage(self):
        return GreenTea()


class BlackTeaFactory(IFactory):
    def create_beverage(self):
        return BlackTea()


class MilkTeaFactory(IFactory):
    def create_beverage(self):
        return MilkTea()


# Store
class BeverageStore:
    def __init__(self, factory):
        self.__factory = factory

    def order_beverage(self):
        beverage = self.__factory.create_beverage()

        beverage.add_material()
        beverage.brew()
        beverage.poured_cup()


def main():
    store = BeverageStore(MilkTeaFactory())
    store.order_beverage()

    store = BeverageStore(GreenTeaFactory())
    store.order_beverage()


if __name__ == '__main__':
    main()
