""" Created by wu.jieyi on 2016/03/11. """
from abc import ABCMeta, abstractmethod


class Mediator(metaclass=ABCMeta):
    """
    Mediator class. Connection of all Person class.
    """

    @abstractmethod
    def contact(self, sender, msg):
        pass


class Person(metaclass=ABCMeta):
    """
    Basic Person class.
    Each of Person have to keep a mediator for connecting
    each other.
    """

    def __init__(self, name, mediator):
        self.mediator = mediator
        self.name = name

    def contact(self, msg):
        self.mediator.contact(self, msg)

    @abstractmethod
    def get_message(self, msg):
        pass


class Owner(Person):
    def __init__(self, name, mediator):
        super(Owner, self).__init__(name, mediator)
        self.mediator.register_owner(self)

    def get_message(self, msg):
        print('Owner', self.name, ', get a msg:', msg)


class Renter(Person):
    def __init__(self, name, mediator):
        super(Renter, self).__init__(name, mediator)
        self.mediator.register_renter(self)

    def get_message(self, msg):
        print('Renter', self.name, ', get a msg:', msg)


class RealEstateBroker(Mediator):
    def __init__(self):
        self.owner = None
        self.renter = None

    def contact(self, sender, msg):
        if sender is self.owner:
            self.renter.get_message(msg)
        elif sender is self.renter:
            self.owner.get_message(msg)

    def register_owner(self, owner):
        self.owner = owner

    def register_renter(self, renter):
        self.renter = renter


def main():
    broker = RealEstateBroker()

    wu = Owner('Jieyi', broker)
    chen = Renter('Pipi', broker)

    wu.contact('I wanna rent this to someone.')
    chen.contact("Cool! I'm just search the apartment.")


if __name__ == '__main__':
    main()
