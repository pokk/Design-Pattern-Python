""" Created by wu.jieyi on 2016/03/22. """
from abc import ABCMeta, abstractmethod


# Compoent.
class Employee(metaclass=ABCMeta):
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @abstractmethod
    def add_employee(self, employee):
        pass

    @abstractmethod
    def remove_employee(self, employee):
        pass

    def show(self, depth):
        print('**' * depth, 'name:', self._name, 'salary:', self._salary)
        print('-------------------------')


# Composite.
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.developer_list = []

    def add_employee(self, employee):
        self.developer_list.append(employee)

    def remove_employee(self, employee):
        self.developer_list.remove(employee)

    def show(self, depth):
        super(Manager, self).show(depth)

        # Foreach to children.
        for ep in self.developer_list:
            ep.show(depth + 1)


# Leaf.
class Programmer(Employee):
    def add_employee(self, employee):
        pass

    def remove_employee(self, employee):
        pass


def main():
    manager = Manager('Jieyi', 1200000)
    manager.add_employee(Programmer('Nancy', 800000))
    manager.add_employee(Programmer('Peter', 500000))
    programmer_one = Programmer('Ted', 760000)
    programmer_two = Programmer('Andy', 650000)

    general_manager = Manager('Root', 0)  # Root node, nothing to do.
    general_manager.add_employee(manager)
    general_manager.add_employee(programmer_one)
    general_manager.add_employee(programmer_two)

    general_manager.show(0)


if __name__ == '__main__':
    main()
