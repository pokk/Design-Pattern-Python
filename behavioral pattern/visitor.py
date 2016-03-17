""" Created by wu.jieyi on 2016/03/17. """
from abc import ABCMeta, abstractmethod


# Element abstract.
class Hardware(metaclass=ABCMeta):
    def __init__(self):
        self.price = None

    @abstractmethod
    def accept(self, visitor):
        pass


class MainBoard(Hardware):
    def __init__(self):
        super().__init__()
        self.price = 32

    def accept(self, visitor):
        visitor.visit(self)


class Memory(Hardware):
    def __init__(self):
        super().__init__()
        self.price = 70

    def accept(self, visitor):
        visitor.visit(self)


class Display(Hardware):
    def __init__(self):
        super().__init__()
        self.price = 120

    def accept(self, visitor):
        visitor.visit(self)


class NetworkAdapter(Hardware):
    def __init__(self):
        super().__init__()
        self.price = 20

    def accept(self, visitor):
        visitor.visit(self)


# Object structure.
class Computer(Hardware):
    def __init__(self):
        super().__init__()
        self.part = []

    def add_parts(self, element):
        self.part.append(element)

    def accept(self, visitor):
        for p in self.part:
            p.accept(visitor)


# Visitor abstract.
class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, element):
        pass


class PriceVisitor(Visitor):
    def __init__(self):
        self.amount = 0

    def visit(self, element):
        self.amount += element.price


def main():
    computer = Computer()
    computer.add_parts(Memory())
    computer.add_parts(MainBoard())
    computer.add_parts(NetworkAdapter())
    computer.add_parts(Display())

    p = PriceVisitor()
    computer.accept(p)
    print(p.amount)


if __name__ == '__main__':
    main()
