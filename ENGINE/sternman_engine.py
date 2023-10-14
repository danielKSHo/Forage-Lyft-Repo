from ENGINE.engine import Engine

class CapuletEngine(Engine):
    
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service() -> bool:
        pass
