""" Created by Jieyi on 1/27/16. """
from abc import ABCMeta, abstractmethod


# Abstract class
class CheckLabel(metaclass=ABCMeta):
	"""
	Base of check handler abstract.
	"""

	def __init__(self, nextCheckRule):
		self._nextRule = nextCheckRule

	@abstractmethod
	def Checking(self, label):
		...


class CheckLength(CheckLabel):
	"""
	One of the checking condition. For string length.
	"""

	def Checking(self, label):
		if len(label.content) > 10:
			print("Ok you passed length!!")
		else:
			if self._nextRule is not None:
				self._nextRule.Checking(label)


class CheckBigAlphabet(CheckLabel):
	"""
	One of the checking condition. For big alphabet.
	"""

	def Checking(self, label):
		if label.content.isupper():
			print("Ok you passed upper!!")
		else:
			if self._nextRule is not None:
				self._nextRule.Checking(label)
			else:
				print("no any pass!!!!")


class SpecialLabel:
	"""
	The object is be applied.
	"""

	def __init__(self, content):
		self.__content = content

	@property
	def content(self):
		return self.__content

	@content.setter
	def content(self, value):
		self.__content = value


def main():
	s1 = SpecialLabel("no")
	s2 = SpecialLabel("Oh suck man")
	s3 = SpecialLabel("SUPERMAN")

	checking = CheckLength(CheckBigAlphabet(None))
	checking.Checking(s1)

	checking.Checking(s2)

	checking.Checking(s3)


if __name__ == '__main__':
	main()
