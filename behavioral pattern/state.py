""" Created by wu.jieyi on 2016/03/14. """
from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    """
    State's interface.
    There are
    four actions: book_room, unsubscribe_room, check_in_room, check_out_room
    three states: FreeTimeState, CheckInState, BookedState
    """

    def __init__(self, hotel_manager):
        self._manager = hotel_manager

    @abstractmethod
    def book_room(self):
        pass

    @abstractmethod
    def unsubscribe_room(self):
        pass

    @abstractmethod
    def check_in_room(self):
        pass

    @abstractmethod
    def check_out_room(self):
        pass


class Room:
    """
    Context. Here is including state member.
    """

    def __init__(self):
        self._state = FreeTimeState(self)

    # Request booking.
    def book(self):
        self._state.book_room()

    # Request unsubscribing.
    def unsubscribe(self):
        self._state.unsubscribe_room()

    # Request checking in.
    def check_in(self):
        self._state.check_in_room()

    # Request checking out.
    def check_out(self):
        self._state.check_out_room()

    def show_state(self):
        print('now state is:', self._state.__class__.__name__)

    @property
    def state(self):
        return self._state

    # Set state.
    @state.setter
    def state(self, value):
        self._state = value


# There are state as below class.
class FreeTimeState(State):
    """
    Free time state for room.
    """

    def unsubscribe_room(self):
        pass

    def check_in_room(self):
        print('You has already checked in...')
        self._manager.state = CheckInState(self._manager)

    def book_room(self):
        print('You booked a room...')
        self._manager.state = BookedState(self._manager)

    def check_out_room(self):
        pass


class CheckInState(State):
    """
    Check in state for room.
    """

    def unsubscribe_room(self):
        pass

    def check_in_room(self):
        print('Someone has already stayed here...')

    def book_room(self):
        print('Someone has already stayed here, you cannot book it...')

    def check_out_room(self):
        print('You are success to check out...')
        self._manager.state = FreeTimeState(self._manager)


class BookedState(State):
    """
    Booked state for room.
    """

    def unsubscribe_room(self):
        print('You are success to unsubscribe this room, welcome again...')
        self._manager.state = FreeTimeState(self._manager)

    def check_in_room(self):
        print('You are success to check in...')
        self._manager.state = CheckInState(self._manager)

    def book_room(self):
        print('Someone has already booked this room...')

    def check_out_room(self):
        pass


def main():
    room = []
    for _ in range(3):
        room.append(Room())

    room[0].book()
    room[0].check_in()
    room[0].show_state()
    room[0].book()
    room[0].show_state()
    print('-------------------')

    room[1].check_in()
    room[1].book()
    room[1].check_out()
    room[1].book()


if __name__ == '__main__':
    main()
