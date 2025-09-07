class InvalidTransition(Exception):
    pass

class Robot:
    def __init__(self):
        self.state = "OFF"
    
    def power_on(self):
        if self.state == "OFF":
            self.state = "ON"
        else:
            raise InvalidTransition(f"No se puede encender el robot desde {self.state}")
    
    def power_off(self):
        if self.state == "ON":
            self.state == "OFF"
        else :
            raise InvalidTransition(f"No se puede apagar el robot desde {self.state}")
    
    def error(self):
        if self.state == "ON":
            self.state = "ERROR"
        else:
            raise InvalidTransition(f"No puede fallar desde {self.state}")

    def reset(self):
        if self.state == "ERROR":
            self.state == "OFF"
        else:
            raise InvalidTransition(f"No puede resetear desde {self.state}")
            