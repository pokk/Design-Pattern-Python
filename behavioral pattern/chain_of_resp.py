""" Created by Jieyi on 1/27/16. """
from abc import ABCMeta, abstractmethod


# Abstract class
class CheckLabelRule(metaclass=ABCMeta):
    """
    Abstract of the check conditions.
    """

    def __init__(self, next_rule):
        self.__checkRule = next_rule

    def checking(self, label):
        if self.is_my_resp(label):
            self.do_check(label)
        # If I take off this else, the process will be processed to the end.
        # You can adjust by yourself, what the kind of case you wanna do.
        else:
            if self.__checkRule is not None:
                self.__checkRule.checking(label)
            else:
                print('Finished check')

    # Do something which the case needs to do.
    @abstractmethod
    def do_check(self, label):
        pass

    # checking who will do something.
    @abstractmethod
    def is_my_resp(self, label):
        pass


# checking condition.
class CheckLength(CheckLabelRule):
    """
    One of the checking condition. For string length.
    """

    def is_my_resp(self, label):
        return label.name == 'tel_label'

    def do_check(self, label):
        if len(label.content) <= 6 or len(label.content) >= 20:
            print("over the length range.")
        else:
            print("you pass the length testing")


# checking condition.
class CheckBigAlphabet(CheckLabelRule):
    """
    One of the checking condition. For big alphabet.
    """

    def is_my_resp(self, label):
        return label.name == 'name_label'

    def do_check(self, label):
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

    rule.checking(Label("tel_label", "12345678"))
    rule.checking(Label("name_label", "abcdef"))


if __name__ == '__main__':
    main()
