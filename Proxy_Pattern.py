__author__ = 'pi'

from abc import ABCMeta


# abstract
class IGiveGit(metaclass=ABCMeta):
    def give_eyes(self):
        ...

    def give_foots(self):
        ...

    def give_arms(self):
        ...


# idiot man
class PoorPursuit(IGiveGit):
    woman = None

    def __init__(self, girl):
        self.woman = girl

    def give_eyes(self):
        print("送給 " + self.woman.get_name() + " 我的眼啦，都給你啦")

    def give_foots(self):
        print("送給 " + self.woman.get_name() + " 我的雙腳啦，都給你啦")

    def give_arms(self):
        print("送給 " + self.woman.get_name() + " 我的手啦，通通都給你啦")


# proxy man
class ProxyMan(IGiveGit):
    ggMan = None

    def __init__(self, girl):
        self.ggMan = PoorPursuit(girl)

    def give_eyes(self):
        self.ggMan.give_eyes()

    def give_foots(self):
        self.ggMan.give_foots()

    def give_arms(self):
        self.ggMan.give_arms()


# hot girl
class BeautifulGirl():
    __name = []

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value


def main():
    girl = BeautifulGirl()
    girl.set_name("韓湘嫦")

    proxy = ProxyMan(girl)

    proxy.give_eyes()
    proxy.give_foots()
    proxy.give_arms()

    pass


if __name__ == "__main__":
    main()
