__author__ = 'pi'

from abc import ABCMeta


# observer base class
class Observer(metaclass=ABCMeta):
	def Update(self):
		...


# if observer was added, just create a new class to inherit base class
class ConcreteObserver(Observer):
	def __init__(self, subject, name):
		self.name = name
		self.subject = subject
		self.observerState = []

	# override function
	def Update(self):
		self.observerState = self.subject.get_subjectState()
		print("觀察者 " + self.name + " 的新狀態是 " + self.observerState)

	# get function
	def get_observerState(self):
		return self.observerState

	# set function
	def set_observerState(self, value):
		self.observerState = value


# subject base class
class Subject:
	__observers = []  # observer list

	# add the observer into list
	def Attach(self, obj):
		self.__observers.append(obj)
		pass

	# remove the observer from list
	def Detach(self, obj):
		self.__observers.remove(obj)
		pass

	# notify all of the list
	def Notify(self):
		for obj in self.__observers:
			obj.Update()
		pass


# if subject was changed, just create a new class to inherit base class
class ConcreteSubject(Subject):
	__subjectState = []

	# get function
	def get_subjectState(self):
		return self.__subjectState

	# set function
	def set_subjectState(self, value):
		self.__subjectState = value


def main():
	s = ConcreteSubject()

	s.Attach(ConcreteObserver(s, "小狗"))
	s.Attach(ConcreteObserver(s, "小貓"))
	s.Attach(ConcreteObserver(s, "小肥宅"))

	s.set_subjectState("你的OOXX媽媽來囉~~~")
	s.Notify()


if __name__ == "__main__":
	main()
