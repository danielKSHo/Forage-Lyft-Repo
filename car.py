from ENGINE.engine import Engine
from BATTERY.battery import Battery

class Car():
    
    def __init__(self):
        self.engine = Engine()
        self.battery = Battery()
        
    def needs_service() -> bool:
        pass
