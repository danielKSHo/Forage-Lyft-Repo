from car import Car
from datetime import datetime

class CarFactory():
    
    def create_calliope(self, current_date: datetime, last_service_date: datetime, 
                        current_mileage: int, last_service_mileage: int) -> Car:
        pass
    
    def create_glissade(self, current_date: datetime, last_service_date: datetime, 
                        current_mileage: int, last_service_mileage: int) -> Car:
        pass
    
    def create_palindrome(self, current_date: datetime, last_service_date: datetime, 
                          warning_light_on: bool) -> Car:
        pass
    
    def create_rorschach(self, current_date: datetime, last_service_date: datetime, 
                         current_mileage: int, last_service_mileage: int) -> Car:
        pass
    
    def create_thovex(self, current_date: datetime, last_service_date: datetime, 
                      current_mileage: int, last_service_mileage: int) -> Car:
        pass