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
    def get_content(self):
        ...


class FriedChicken(Meal):
    """
    Main meal: Fried Chicken.
    """

    def price(self):
        return 49.0

    def get_content(self):
        return 'Fried Chicken'


class Hamburger(Meal):
    """
    Main meal: Hamburger
    """

    def price(self):
        return 99.0

    def get_content(self):
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

    def get_content(self):
        return self._meal.get_content() + ', Salad'


class Coke(SideDish):
    """
    Decorator: Add the some side dish.
    """

    def __init__(self, meal):
        super(Coke, self).__init__(meal)

    def price(self):
        return self._meal.price() + 15.0

    def get_content(self):
        return self._meal.get_content() + ', Coke'


def main():
    meal = FriedChicken()
    print("meal : %s ; price : %f" % (meal.get_content(), meal.price()))
    meal = Salad(meal)
    print("meal : %s ; price : %f" % (meal.get_content(), meal.price()))
    meal = Coke(meal)
    print("meal : %s ; price : %f" % (meal.get_content(), meal.price()))


if __name__ == '__main__':
    main()
