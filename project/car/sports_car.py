from project.car.car import Car


class SportsCar(Car):
    _MIN_SPEED_LIMIT = 400
    _MAX_SPEED_LIMIT = 600

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)
        self._MIN_SPEED_LIMIT = 400
        self._MAX_SPEED_LIMIT = 600