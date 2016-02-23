""" Created by Jieyi on 1/26/16. """
from abc import ABCMeta, abstractmethod


# Interface for be producted
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


# Factory
class SimpleBeverageFactory:
    def create_beverage(self, beverage_type):
        if beverage_type is 'GreenTea':
            self._beverage = GreenTea()
        elif beverage_type is 'BlackTea':
            self._beverage = BlackTea()
        else:
            pass

        return self._beverage


class BeverageStore():
    def __init__(self, factory):
        self.__factory = factory

    def beverage_order(self, beverage_type):
        beverage = self.__factory.create_beverage(beverage_type)

        beverage.add_material()
        beverage.brew()
        beverage.poured_cup()


def main():
    store = BeverageStore(SimpleBeverageFactory())
    store.beverage_order('GreenTea')
    print('--------------------')
    store.beverage_order('BlackTea')


if __name__ == '__main__':
    main()
