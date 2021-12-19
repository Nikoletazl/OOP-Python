import sys

from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


def create_car(car_type: str, model: str, speed_limit: int):
    if car_type == "SportsCar":
        return SportsCar(model, speed_limit)
    if car_type == "MuscleCar":
        return MuscleCar(model, speed_limit)


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = create_car(car_type, model, speed_limit)

        if self.__find_car_by_model(model):
            raise Exception(f"Car {model} is already created!")

        if car:
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = Driver(driver_name)

        if self.__find_driver_by_name(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = Race(race_name)

        if self.__find_race_by_name(race_name):
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        free_car = self.__find_free_cars(car_type)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not free_car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            free_car.is_taken = True
            driver.car.is_taken = False
            old_model = driver.car.model
            driver.car = free_car
            return f"Driver {driver_name} changed his car from {old_model} to {driver.car.model}."

        if driver.car is None:
            free_car.is_taken = True
            driver.car = free_car
            return f"Driver {driver_name} chose the car {free_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race_by_name(race_name)
        driver = self.__find_driver_by_name(driver_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if not self.__check_if_driver_exists(driver_name, race_name):
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        drivers = [driver for driver in race.drivers]

        fastest_drivers = {}
        for driver in drivers:
            fastest_drivers[driver.name] = driver.car.speed_limit

        counter = 0
        result = ""
        for key, value in sorted(fastest_drivers.items(), key=lambda x: x[1], reverse=True):
            if counter < 3:
                for driver in drivers:
                    if driver.name == key:
                        driver.number_of_wins += 1
                result += f"Driver {key} wins the {race_name} race with a speed of {value}.\n"
            counter += 1

        return result.strip()

    def __find_free_cars(self, car_type):
        car = [car for car in self.cars if car.__class__.__name__ == car_type and car.is_taken is False]
        if car:
            return car[-1]

    def __find_car_by_model(self, model):
        for car in self.cars:
            if car.model == model:
                return car

    def __find_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def __find_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

    def __check_if_driver_exists(self, driver_name, race_name):
        driver = self.__find_driver_by_name(driver_name)
        race = self.__find_race_by_name(race_name)

        if driver not in race.drivers:
            return driver






