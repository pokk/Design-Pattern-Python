""" Created by wu.jieyi on 2016/03/11. """
import time
from copy import deepcopy


class Record:
    """
    Memento class for keeping various data states.
    """

    def __init__(self, state):
        self.data = state
        self.date = time.ctime()


class Role:
    """
    Originator class. Here is a game role for saving the role state.
    """

    class RoleState:
        """
        All of role state we want to keep.
        """

        def __init__(self, hp, mp):
            self.hp = hp
            self.mp = mp

    def __init__(self, role_state):
        self.role_state = role_state

    def show(self):
        print('HP:', self.role_state.hp)
        print('MP:', self.role_state.mp)

    def save_status(self):
        return Record(deepcopy(self.role_state))

    def load_status(self, backup):
        self.role_state = backup


class Recovery:
    """
    Caretaker for manager the keeping and the loading.
    Depend on the status, you can omit this.
    """

    def __init__(self):
        self.memento_list = []

    # Similar to set function.
    def save(self, memento):
        self.memento_list.append(memento)

    # Similar to get function.
    def load(self, memo):
        for m in self.memento_list:
            if m is memo:
                self.memento_list.remove(m)
                return m.data
        return None


def main():
    newbie = Role(Role.RoleState(100, 100))
    re = Recovery()

    print('====== init status ======')
    newbie.show()
    # Save the status.
    record_begin = newbie.save_status()
    re.save(record_begin)

    print('====== after the first time fighter ======')
    newbie.role_state.hp = 80
    newbie.role_state.mp = 70
    record_fir = newbie.save_status()
    re.save(record_fir)

    newbie.show()
    print('====== after pk with a small boss ======')
    newbie.role_state.hp = 30
    newbie.role_state.mp = 40
    record_sec = newbie.save_status()
    re.save(record_sec)

    newbie.show()
    print('====== load record ======')
    newbie.load_status(re.load(record_fir))

    newbie.show()


if __name__ == '__main__':
    main()
