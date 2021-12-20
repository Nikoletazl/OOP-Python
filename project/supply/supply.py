from abc import ABC, abstractmethod


class Supply(ABC):
    @abstractmethod
    def __init__(self, name, energy=None):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if value:
            if value < 0:
                raise ValueError("Energy cannot be less than zero.")
        self.__energy = value




