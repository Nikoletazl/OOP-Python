from abc import ABC, abstractmethod


class BaseFish(ABC):
    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        if self.__name == "":
            raise ValueError("Fish name cannot be an empty string.")

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.__species = value
        if self.__species == "":
            raise ValueError("Fish species cannot be an empty string.")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value
        if self.__price <= 0:
            raise ValueError("Price cannot be equal to or below zero.")

    def eat(self):
        self.size += 5
