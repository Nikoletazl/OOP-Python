from project.car.car import Car


class MuscleCar(Car):
    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    def range_speed(self):
        return [250, 450]
