__author__ = 'pi'

from abc import ABCMeta


# abstract
class IGiveGit(metaclass=ABCMeta):
	def GiveEyes(self):
		...

	def GiveFoots(self):
		...

	def GiveArms(self):
		...


# idiot man
class PoorPursuit(IGiveGit):
	woman = None

	def __init__(self, girl):
		self.woman = girl

	def GiveEyes(self):
		print("送給 " + self.woman.get_name() + " 我的眼啦，都給你啦")

	def GiveFoots(self):
		print("送給 " + self.woman.get_name() + " 我的雙腳啦，都給你啦")

	def GiveArms(self):
		print("送給 " + self.woman.get_name() + " 我的手啦，通通都給你啦")


# proxy man
class ProxyMan(IGiveGit):
	ggMan = None

	def __init__(self, girl):
		self.ggMan = PoorPursuit(girl)

	def GiveEyes(self):
		self.ggMan.GiveEyes()

	def GiveFoots(self):
		self.ggMan.GiveFoots()

	def GiveArms(self):
		self.ggMan.GiveArms()


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

	proxy.GiveEyes()
	proxy.GiveFoots()
	proxy.GiveArms()

	pass


if __name__ == "__main__":
	main()
