""" Created by Jieyi on 3/10/16. """
from abc import ABCMeta, abstractmethod


class CaffeineBeverage(metaclass=ABCMeta):
    def __init__(self):
        pass

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print('Boiling water...')

    def pour_in_cup(self):
        print('Pouring into Cup...')

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass


class Coffee(CaffeineBeverage):
    def add_condiments(self):
        print('Adding Sugar and Milk...')

    def brew(self):
        print('Dripping Coffee through filter...')


class Tea(CaffeineBeverage):
    def add_condiments(self):
        print('Adding Lemon...')

    def brew(self):
        print('Steeping the tea...')


def main():
    coffee = Coffee()
    coffee.prepare_recipe()

    print('=================================')

    tea = Tea()
    tea.prepare_recipe()


if __name__ == '__main__':
    main()
