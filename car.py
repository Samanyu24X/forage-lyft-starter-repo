from abc import ABC, abstractmethod
from battery.battery import Battery
from engine.engine import Engine
from serviceable import Serviceable

class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
