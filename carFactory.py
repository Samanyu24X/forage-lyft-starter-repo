from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires
from car import Car

# the instructions never specified which car models to assign to each tire, so I have assigned them myself

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire_sensors)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire_sensors)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_sensors):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire_sensors)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tire_sensors)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tire_sensors)
        car = Car(engine, battery, tires)
        return car