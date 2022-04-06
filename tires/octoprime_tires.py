from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_sensors):
        self.tire_sensors = tire_sensors

    def needs_service(self):
        sum = 0
        for sensor in self.tire_sensors:
            sum += sensor
        if sum >= 3:
            return True
        else:
            return False