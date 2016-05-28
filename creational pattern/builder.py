""" Created by wu.jieyi on 2016/02/23. """
from abc import ABCMeta, abstractmethod


class Meal:
    def __init__(self):
        self.salad = None
        self.soup = None
        self.food = None
        self.drink = None

    def __str__(self):
        return 'Salad: %s,  Soup: %s,  Food: %s,  Drink: %s' % (self.salad, self.soup, self.food, self.drink)


class MealBuilder(metaclass=ABCMeta):
    def __init__(self):
        self.meal = Meal()

    @abstractmethod
    def build_salad(self):
        pass

    @abstractmethod
    def build_soup(self):
        pass

    @abstractmethod
    def build_food(self):
        pass

    @abstractmethod
    def build_drink(self):
        pass

    @property
    def create_meal(self):
        return self.meal


class MealSetA(MealBuilder):
    def build_food(self):
        self.meal.food = 'Steak'

    def build_soup(self):
        self.meal.soup = 'Corn Chowder'

    def build_drink(self):
        self.meal.drink = 'Coffee'

    def build_salad(self):
        self.meal.salad = 'Caesar Salad'


class MealSetB(MealBuilder):
    def build_food(self):
        self.meal.food = 'Fish Burger'

    def build_soup(self):
        self.meal.soup = 'Seafood Soup'

    def build_drink(self):
        self.meal.drink = 'Orange Juice'

    def build_salad(self):
        self.meal.salad = 'Salad'


class Waiter:
    def __init__(self):
        self.__meal_builder = None

    def concrete(self):
        self.__meal_builder.build_salad()
        self.__meal_builder.build_soup()
        self.__meal_builder.build_food()
        self.__meal_builder.build_drink()

        return self.__meal_builder.create_meal

    @property
    def builder(self):
        return self.__meal_builder

    @builder.setter
    def builder(self, value):
        self.__meal_builder = value


def main():
    waiter = Waiter()
    waiter.builder = MealSetA()
    meal = waiter.concrete()
    print(meal)
    waiter.builder = MealSetB()
    meal = waiter.concrete()
    print(meal)


if __name__ == '__main__':
    main()
