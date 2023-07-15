from math import inf
from typing import List

from .settings import DEFAULT_FLOOR_MAP, SLOTS_MAP
from .vehicle import BaseVehicle
from .ticket import Ticket

class NoParkingSpaceException(Exception):
    """ No Parking Space available """

class ParkingFloor:
    """
    A parking floor can contain one or more types of parking slots
    default:
        trucks = 1
        bikes = 2
        cars = every other slot
    A Vehicle should be parked at the first empty position of its type
    """
    def __init__(self, size, floor_id, *args, **kwargs):
        self.floor_map = (
            DEFAULT_FLOOR_MAP if "floor_map" not in kwargs
            else kwargs["floor_map"]
        )
        self.busy_slot_map = {x: {} for x in self.floor_map.keys()}
        self.id = int(floor_id)
        self.size = int(size)
        self._floorMapSetup()

    def _floorMapSetup(self):
        """clear inf value from floor_map"""
        for value in self.floor_map.values():
            if value[1] == inf:
                value[1] = self.size + 1
    
    def _firstEmptyParkingSlot(self, vehicle) -> int:
        """find first empty slot for vehicle class"""
        slot_range = self.floor_map[vehicle]
        for x in range(slot_range[0], slot_range[1]):
            if x not in self.busy_slot_map[vehicle]:
                return x
        return -1
    
    def parkVehicle(self, vehicle: BaseVehicle) -> Ticket: # parkVehicle takes two parameters and return the an object type "Ticket"
        """park vehicle in first empty slot"""
        minSlotValue = self._firstEmptyParkingSlot(type(vehicle))
        if minSlotValue == -1:
            raise NoParkingSpaceException()
        