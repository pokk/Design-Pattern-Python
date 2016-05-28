""" Created by wu.jieyi on 2016/03/14. """
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


# Observer base class
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, msg):
        pass


# If observer was added, just create a new class to inherit base class
class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print("observer: " + self.name + " the newest state is " + msg)


# Subject base class
class Subject(metaclass=ABCMeta):
    # Add the observer into list
    @abstractmethod
    def attach(self, obj):
        pass

    # Remove the observer from list
    @abstractmethod
    def detach(self, obj):
        pass

    # Notify all of the list
    @abstractmethod
    def notify(self, msg):
        pass


# If subject was changed, just create a new class to inherit base class
class ConcreteSubject(Subject):
    def __init__(self):
        self.__observers = []  # observer list

    def notify(self, msg):
        for obj in self.__observers:
            obj.update(msg)

    def detach(self, obj):
        self.__observers.remove(obj)

    def attach(self, obj):
        self.__observers.append(obj)


def main():
    s = ConcreteSubject()

    s.attach(ConcreteObserver("Poppy"))
    s.attach(ConcreteObserver("Catty"))
    s.attach(ConcreteObserver("Nerdy"))

    s.notify("Your mom is coming here!!!")
    print('-----------------------------------')
    s.notify("I am escaping...")

if __name__ == "__main__":
    main()
