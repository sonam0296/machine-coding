from math import inf

from .slot import BikeSlot, CarSlot, TruckSlot
from .vehicle import Car, Bike, Truck

SLOTS_MAP = {Truck: TruckSlot, Bike: BikeSlot, Car: CarSlot}

VEHICLES_MAP = {"CAR": Car, "BIKE": Bike, "TRUCK": Truck}

DEFAULT_FLOOR_MAP = {Truck: [1, 2], Bike: [2, 4], Car: [4, inf]}