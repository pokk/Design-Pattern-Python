""" Created by wu.jieyi on 2016/03/08. """
from abc import ABCMeta, abstractmethod


class Rectangle(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# Adaptee.
class LegacyRectangle:
    def __init__(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

    def legacy_draw(self):
        print('Legacy onDraw()')
        print('x1:', self._x1, 'x2:', self._x2, 'y1:', self._y1, 'y2:', self._y2)


# Adapter.
class RectangleAdapter(Rectangle):
    def __init__(self, x, y, w, h):
        self._rectangle = LegacyRectangle(x, y, x + w, y + h)

    def draw(self):
        self._rectangle.legacy_draw()


def main():
    rec = RectangleAdapter(10, 30, 15, 20)
    rec.draw()


if __name__ == '__main__':
    main()
