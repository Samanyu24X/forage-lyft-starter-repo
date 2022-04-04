from abc import ABC
from battery import Battery
from datetime import datetime
from dateutil.relativedelta import relativedelta

class SpindlerBattery(Battery, ABC):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        next_service_date = self.last_service_date + relativedelta(years=2)
        return self.current_date > next_service_date
