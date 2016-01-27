""" Created by Jieyi on 1/27/16. """
from abc import ABCMeta, abstractmethod


# Abstract class
class CheckLabelRule(metaclass=ABCMeta):
	"""
	Abstract of the check conditions.
	"""

	def __init__(self, nextRule):
		self.__checkRule = nextRule

	def Checking(self, label):
		if self.isMyResp(label):
			self.doCheck(label)
		# If I take off this else, the process will be processed to the end.
		# You can adjust by yourself, what the kind of case you wanna do.
		else:
			if self.__checkRule is not None:
				self.__checkRule.Checking(label)
			else:
				print('Finished check')

	# Do something which the case needs to do.
	@abstractmethod
	def doCheck(self, label):
		...

	# Checking who will do something.
	@abstractmethod
	def isMyResp(self, label):
		...


# Checking condition.
class CheckLength(CheckLabelRule):
	"""
	One of the checking condition. For string length.
	"""

	def isMyResp(self, label):
		return label.name == 'tel_label'

	def doCheck(self, label):
		if len(label.content) <= 6 or len(label.content) >= 20:
			print("over the length range.")
		else:
			print("you pass the length testing")


# Checking condition.
class CheckBigAlphabet(CheckLabelRule):
	"""
	One of the checking condition. For big alphabet.
	"""

	def isMyResp(self, label):
		return label.name == 'name_label'

	def doCheck(self, label):
		if not label.content.isupper():
			print("you have to set big alphabet string")
		else:
			print("you pass the alphabet testing")


# Client object
class Label:
	"""
	The object is checked by chain of resp.
	"""

	def __init__(self, name, content):
		self.name = name
		self.content = content


def main():
	rule = CheckLength(CheckBigAlphabet(None))

	rule.Checking(Label("tel_label", "12345678"))
	rule.Checking(Label("name_label", "abcdef"))


if __name__ == '__main__':
	main()
