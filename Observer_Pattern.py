__author__ = 'pi'

from abc import ABCMeta


# observer base class
class Observer(metaclass=ABCMeta):
	def update(self):
		...


# if observer was added, just create a new class to inherit base class
class ConcreteObserver(Observer):
	def __init__(self, subject, name):
		self.name = name
		self.subject = subject
		self.observerState = []

	# override function
	def update(self):
		self.observerState = self.subject.get_subject_state()
		print("觀察者 " + self.name + " 的新狀態是 " + self.observerState)

	# get function
	def get_observer_state(self):
		return self.observerState

	# set function
	def set_observer_state(self, value):
		self.observerState = value


# subject base class
class Subject:
	__observers = []  # observer list

	# add the observer into list
	def attach(self, obj):
		self.__observers.append(obj)
		pass

	# remove the observer from list
	def detach(self, obj):
		self.__observers.remove(obj)
		pass

	# notify all of the list
	def notify(self):
		for obj in self.__observers:
			obj.update()
		pass


# if subject was changed, just create a new class to inherit base class
class ConcreteSubject(Subject):
	__subjectState = []

	# get function
	def get_subject_state(self):
		return self.__subjectState

	# set function
	def set_subject_state(self, value):
		self.__subjectState = value


def main():
	s = ConcreteSubject()

	s.attach(ConcreteObserver(s, "小狗"))
	s.attach(ConcreteObserver(s, "小貓"))
	s.attach(ConcreteObserver(s, "小肥宅"))

	s.set_subject_state("你的OOXX媽媽來囉~~~")
	s.notify()


if __name__ == "__main__":
	main()
