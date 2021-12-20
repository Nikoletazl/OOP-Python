from project.supply.supply import Supply


class Food(Supply):
    def __init__(self, name, *args):
        super().__init__(name)
        self._energy(*args)

    def _energy(self, *args):
        if not args:
            self.energy = 25
        else:
            self.energy = args[0]
