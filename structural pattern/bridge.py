""" Created by wu.jieyi on 2016/03/08. """
from abc import ABCMeta, abstractmethod


# Abstraction.
class AngryAnimal(metaclass=ABCMeta):
    def __init__(self, physic_engine):
        self._physic_engine = physic_engine

    @abstractmethod
    def play(self):
        pass


# Refined Abstraction.
class AngryBird(AngryAnimal):
    def play(self):
        print('AngryBird collide with blocks using', self._physic_engine.collide())


# Refined Abstraction.
class AngryDog(AngryAnimal):
    def play(self):
        print('AngryDog collide with blocks using', self._physic_engine.collide())


# Implementor.
class IEngine(metaclass=ABCMeta):
    @abstractmethod
    def collide(self):
        pass


class PhysicBigArm(IEngine):
    def collide(self):
        return 'Big Arm physic engine'


class PhysicWeapon(IEngine):
    def collide(self):
        return 'Weapon physic engine'


def main():
    angry_bird_2_3 = AngryBird(PhysicWeapon())
    angry_dog_2_3 = AngryDog(PhysicWeapon())

    angry_bird_2_3.play()
    angry_dog_2_3.play()

    angry_bird_2_4 = AngryBird(PhysicBigArm())

    angry_bird_2_4.play()


if __name__ == '__main__':
    main()
