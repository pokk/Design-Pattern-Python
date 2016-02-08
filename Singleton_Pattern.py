""" Created by Jieyi on 1/19/16. """


class Singleton:
	"""
	Classic Singleton pattern.
	"""
	__instance = None

	def __new__(cls, *args, **kwargs):
		if not cls.__instance:
			cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

		return cls.__instance


class Borg:
	"""
	Classic Borg pattern. (similar to Singleton pattern  *The functions are the same)
	"""
	__share_state = {}

	def __init__(self):
		self.__dict__ = self.__share_state


# Classic Singleton's example
def singleton_ex():
	s1 = Singleton()
	s1.name = 'Singleton'
	s2 = Singleton()
	print(s1, s2)
	print(s1.name, s2.name)

	s2.num = 94
	print(s1.num, s2.num)
	s1.num = 20
	print(s1.num, s2.num)


# Borg pattern(Google Singleton)'s example
def borg_ex():
	b1 = Borg()
	b1.name = 'Borg'
	b2 = Borg()
	print(b1, b2)
	print(b1.name, b2.name)

	b2.num = 20
	print(b1.num, b2.num)

	b3 = Borg()
	print(b3.num, b1.num, b2.num)


def main(pattern):
	ex = pattern
	{
		1: lambda: borg_ex(),
		2: lambda: singleton_ex(),
	}.get(pattern, lambda: None)()


if __name__ == '__main__':
	pattern = 2
	main(pattern)
