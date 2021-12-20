class Player:

    def __init__(self, name, age, stamina=None):
        self._need_sustenance = True
        self.stamina = stamina
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value:
            if value < 0 or value > 100:
                raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self._need_sustenance
