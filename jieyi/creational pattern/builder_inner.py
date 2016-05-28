""" Created by wu.jieyi on 2016/02/29. """


class Meal:
    def __init__(self):
        self.salad = None
        self.soup = None
        self.food = None
        self.drink = None

    def __str__(self):
        return 'Salad: %s,  Soup: %s,  Food: %s,  Drink: %s' % (self.salad, self.soup, self.food, self.drink)

    class MealBuilder:
        def __init__(self):
            self.__meal = Meal()

        def set_salad(self, salad):
            self.__meal.salad = salad
            return self

        def set_soup(self, soup):
            self.__meal.soup = soup
            return self

        def set_food(self, food):
            self.__meal.food = food
            return self

        def set_drink(self, drink):
            self.__meal.drink = drink
            return self

        def build(self):
            return self.__meal


class MealSet:
    def __init__(self):
        self.__meal = Meal()

    def a(self):
        self.__meal = Meal.MealBuilder(). \
            set_soup('Seafood soup'). \
            set_salad('Casar Salad'). \
            set_food('Lobster'). \
            set_drink('Black Tea').build()

        return self.__meal

    def b(self):
        self.__meal = Meal.MealBuilder(). \
            set_soup('Crown Chowder'). \
            set_salad('Bibi Salad'). \
            set_food('Big Fish'). \
            set_drink('Coffee').build()

        return self.__meal


def main():
    meal = MealSet().b()
    print('Set A:', meal)
    meal = MealSet().a()
    print('Set B:', meal)


if __name__ == '__main__':
    main()
