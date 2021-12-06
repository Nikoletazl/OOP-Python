from abc import ABC, abstractmethod
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        if self.__name == "":
            raise ValueError("Aquarium name cannot be an empty string.")

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    def calculate_comfort(self):
        pass


    def add_fish(self, fish):
        if self.__capacity < len(self.fish):
            return "Not enough capacity."
        else:
            if fish == "FreshwaterFish" or fish == "SaltwaterFish":
                self.fish.append(SaltwaterAquarium)
                return f"Successfully added {fish} to {self.name}."

    def remove_fish(self, fish):
        for fish_name in self.fish:
            if fish_name == fish:
                self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            BaseFish.eat(fish)

    def __str__(self):
        return f"""{self.name}:
Fish: {' '.join(x for x in self.fish)}
Decoration: {len(self.decorations)}
Comfort: {self.calculate_comfort}"""