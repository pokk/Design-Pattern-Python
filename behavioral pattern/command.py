""" Created by wu.jieyi on 2016/03/14. """
from abc import ABCMeta, abstractmethod


class Drawing(metaclass=ABCMeta):
    """
    This is not including in command pattern.
    We can add some function for doing easier.
    """

    @abstractmethod
    def process_pen(self):
        pass

    @abstractmethod
    def process_brush(self):
        pass

    @abstractmethod
    def process_blur(self):
        pass


class DrawEffect(Drawing):
    def process_blur(self):
        print("do the blur process...")

    def process_brush(self):
        print("do the brush process...")

    def process_pen(self):
        print("do the pen process...")


class Command(metaclass=ABCMeta):
    """
    Command interface.
    """

    @abstractmethod
    def exec(self, drawing):
        pass


class AEffectCommand(Command):
    """
    Command concrete.
    """

    def exec(self, drawing):
        drawing.process_blur()
        drawing.process_brush()


class BEffectCommand(Command):
    """
    Command concrete.
    """

    def exec(self, drawing):
        drawing.process_pen()
        drawing.process_brush()


class CEffectCommand(Command):
    """
    Command concrete.
    """

    def exec(self, drawing):
        drawing.process_brush()
        drawing.process_blur()


class Invoker:
    """
    Invoker & Receiver.
    """

    def __init__(self):
        self.commands = {}
        self.draw_effect = DrawEffect()

    # Add the command in the list.
    def add_command(self, name, command):
        self.commands[str(name)] = command

    # Execute the command.
    def do_effect(self, name):
        self.commands.get(str(name), None).exec(None, self.draw_effect)


def main():
    invoker = Invoker()
    invoker.add_command('effect A', AEffectCommand)
    invoker.add_command('effect B', BEffectCommand)
    invoker.add_command('effect C', CEffectCommand)

    print('==== Effect A ====')
    invoker.do_effect('effect A')
    print('==== Effect B ====')
    invoker.do_effect('effect B')
    print('==== Effect C ====')
    invoker.do_effect('effect C')


if __name__ == '__main__':
    main()
