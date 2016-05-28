__author__ = 'pi'

from abc import ABCMeta, abstractmethod


# abstract
class IGiveGit(metaclass=ABCMeta):
    @abstractmethod
    def give_glasses(self):
        pass

    @abstractmethod
    def give_boots(self):
        pass

    @abstractmethod
    def give_gloves(self):
        pass


# idiot man
class PoorPursuit(IGiveGit):
    def __init__(self, girl):
        self.woman = girl

    def give_glasses(self):
        print('send', self.woman.get_name(), 'sun glasses')

    def give_boots(self):
        print('send', self.woman.get_name(), 'boots')

    def give_gloves(self):
        print('send', self.woman.get_name(), 'heart gloves')


# proxy man
class ProxyMan(IGiveGit):
    def __init__(self, girl):
        self.ggMan = PoorPursuit(girl)

    def give_glasses(self):
        self.ggMan.give_glasses()

    def give_boots(self):
        self.ggMan.give_boots()

    def give_gloves(self):
        self.ggMan.give_gloves()


# hot girl
class BeautifulGirl:
    def __init__(self):
        self._name = ''

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value


def main():
    girl = BeautifulGirl()
    girl.set_name('Sandy')

    proxy = ProxyMan(girl)

    proxy.give_glasses()
    proxy.give_boots()
    proxy.give_gloves()

    pass


if __name__ == "__main__":
    main()
