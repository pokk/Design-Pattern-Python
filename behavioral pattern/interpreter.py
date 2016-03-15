""" Created by wu.jieyi on 2016/03/15. """
from abc import ABCMeta, abstractmethod


# Abstract Expression
class Node(metaclass=ABCMeta):
    @abstractmethod
    def interpreter(self):
        pass


# Terminal Expression.
class ValueNode(Node):
    def __init__(self, value):
        self.value = value

    def interpreter(self):
        return self.value


# Non-terminal Expression.
class SymbolNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @abstractmethod
    def interpreter(self):
        pass


class MulNode(SymbolNode):
    def interpreter(self):
        return self.left.interpreter() * self.right.interpreter()


class ModNode(SymbolNode):
    def interpreter(self):
        return self.left.interpreter() % self.right.interpreter()


class DivNode(SymbolNode):
    def interpreter(self):
        return self.left.interpreter() / self.right.interpreter()


# Context.
class Calculator:
    """
    Class is including interpreter and all of the information.
    """

    def __init__(self):
        self.statement = None
        self.node = None

    def build(self, statement):
        stack = []
        conti = False
        self.statement = statement.split(' ')

        for i in range(len(self.statement)):
            if conti:
                conti = False
                continue

            if self.statement[i] is "*":
                left = stack.pop()
                right = ValueNode(int(self.statement[i + 1]))
                stack.append(MulNode(left, right))
                conti = True
            elif self.statement[i] is "%":
                left = stack.pop()
                right = ValueNode(int(self.statement[i + 1]))
                stack.append(ModNode(left, right))
                conti = True
            elif self.statement[i] is "/":
                left = stack.pop()
                right = ValueNode(int(self.statement[i + 1]))
                stack.append(DivNode(left, right))
                conti = True
            else:
                stack.append(ValueNode(int(self.statement[i])))

        self.node = stack.pop()

    def compute(self):
        return self.node.interpreter()


def main():
    s = "3 * 2 * 4 / 6 % 5"
    cal = Calculator()
    cal.build(s)
    print(cal.compute())


if __name__ == '__main__':
    main()
