class BaseVehicle:
    def __init__(self, regNo, color):
        self.registrationNumber = regNo
        self.color = color

class Car(BaseVehicle):
    pass

class Bike(BaseVehicle):
    pass

class Truck(BaseVehicle):
    pass