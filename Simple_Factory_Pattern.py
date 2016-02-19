""" Created by Jieyi on 1/26/16. """
from abc import ABCMeta, abstractmethod


# Interface for be producted
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


# Factory
class SimpleBeverageFactory:
    def create_beverage(self, beverageType):
        if beverageType is 'GreenTea':
            self._beverage = GreenTea()
        elif beverageType is 'BlackTea':
            self._beverage = BlackTea()
        else:
            pass

        return self._beverage


class BeverageStore():
    def __init__(self, factory):
        self.__factory = factory

    def beverage_order(self, beverageType):
        self.beverage = self.__factory.create_beverage(beverageType)

        self.beverage.add_material()
        self.beverage.brew()
        self.beverage.poured_cup()


def main():
    store = BeverageStore(SimpleBeverageFactory())
    store.beverage_order('GreenTea')
    print('--------------------')
    store.beverage_order('BlackTea')


if __name__ == '__main__':
    main()
