from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_sensors):
        self.tire_sensors = tire_sensors

    def needs_service(self):
        for sensor in self.tire_sensors:
            if sensor >= 0.9:
                return True
        return False