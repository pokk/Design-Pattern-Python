""" Created by Jieyi on 3/21/16. """
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


# Product A interface.
class IBeverageTea(IBeverageProvider):
    @abstractmethod
    def add_material(self):
        pass

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def poured_cup(self):
        pass


class GreenTea(IBeverageTea):
    def add_material(self):
        print('add the green tea')
        pass

    def brew(self):
        print('brew the hot water into green tea cup')
        pass

    def poured_cup(self):
        print('poured green tea to the cup')
        pass


class MilkTea(IBeverageTea):
    def add_material(self):
        print('add the black tea')
        pass

    def brew(self):
        print('brew the hot water and milk into milk tea cup')
        pass

    def poured_cup(self):
        print('poured milk tea to the cup')
        pass


# Product B interface.
class IBeverageCoffee(IBeverageProvider):
    @abstractmethod
    def add_material(self):
        pass

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def poured_cup(self):
        pass


class BlendCoffee(IBeverageCoffee):
    def add_material(self):
        print('add the coffee beans')
        pass

    def brew(self):
        print('brew the hot water and coffee cup')
        pass

    def poured_cup(self):
        print('poured blend coffee to the cup')
        pass


class Cappuccino(IBeverageCoffee):
    def add_material(self):
        print('add the coffee beans')
        pass

    def brew(self):
        print('brew the hot water and coffee milk of a half cup of the coffee')
        pass

    def poured_cup(self):
        print('poured cappuccino to the cup')
        pass


# Factory.
class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_tea(self):
        pass

    @abstractmethod
    def create_coffee(self):
        pass


class TaiwanFactory(IFactory):
    def create_coffee(self):
        return Cappuccino()

    def create_tea(self):
        return MilkTea()


class HKFactory(IFactory):
    def create_coffee(self):
        return BlendCoffee()

    def create_tea(self):
        return GreenTea()


class QuicklyStore:
    def __init__(self):
        self._factory = TaiwanFactory()

    def order_beverage_coffee(self):
        coffee = self._factory.create_coffee()

        coffee.add_material()
        coffee.brew()
        coffee.poured_cup()


class FiftyStore:
    def __init__(self):
        self._factory = HKFactory()

    def order_beverage_tea(self):
        coffee = self._factory.create_tea()

        coffee.add_material()
        coffee.brew()
        coffee.poured_cup()


def main():
    quickly_store = QuicklyStore()
    quickly_store.order_beverage_coffee()

    hk_store = FiftyStore()
    hk_store.order_beverage_tea()


if __name__ == '__main__':
    main()
