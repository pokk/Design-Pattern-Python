""" Created by wu.jieyi on 2016/03/18. """
from abc import abstractmethod, ABCMeta


# Extrinsic State.
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Fly weight.
class IgoChessman(metaclass=ABCMeta):
    # Here set the 'intrinsic state' inside because the same fly weight is consistent.
    def __init__(self):
        self.chess_color = None

    # Operate handler.
    @abstractmethod
    def color(self):
        pass

    # Here set the 'extrinsic state' from outside. We don't keep it in the fly weight, even if it's the same object.
    def display(self, coordination):
        print('This color is', self.color(), ', coordination x:', coordination.x, ', coordination y:', coordination.y)


class BlackIgoChessman(IgoChessman):
    def color(self):
        self.chess_color = 'BLACK'
        return self.chess_color


class WhiteIgoChessman(IgoChessman):
    def color(self):
        self.chess_color = 'WHITE'
        return self.chess_color


# Fly weight factory.
class IgoChessmanFactory:
    __share_state = {}

    def __init__(self):
        # Here using singleton pattern to implement a pool.
        self.__dict__ = self.__share_state
        self.fly_weights = {}

    def add_chess(self, key, chess):
        self._fly_weights_pool(key, chess)

    def get_fly_weights(self, key):
        return self._fly_weights_pool(key)

    def _fly_weights_pool(self, key, chess=None):
        if key in self.fly_weights:
            return self.fly_weights.get(key)
        else:
            self.fly_weights[key] = chess
            return self.fly_weights.get(key)


def main():
    factory = IgoChessmanFactory()
    factory.add_chess('b', BlackIgoChessman())
    factory.add_chess('w', WhiteIgoChessman())

    black1 = factory.get_fly_weights('b')
    black2 = factory.get_fly_weights('b')
    black3 = factory.get_fly_weights('b')

    white1 = factory.get_fly_weights('w')
    white2 = factory.get_fly_weights('w')
    white3 = factory.get_fly_weights('w')

    black1.display(Coordinate(3, 6))
    black2.display(Coordinate(6, 5))
    black3.display(Coordinate(4, 9))

    white1.display(Coordinate(1, 3))
    white2.display(Coordinate(4, 3))
    white3.display(Coordinate(3, 10))


if __name__ == '__main__':
    main()
