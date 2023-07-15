class Vehicle:
    def __init__(self, vehicle_type, registration_number, color):
        self.vehicle_type = vehicle_type
        self.registration_number = registration_number
        self.color = color

class ParkingSlot:
    def __init__(self, slot_type, floor_number, slot_number):
        self.slot_type = slot_type
        self.is_available = True
        self.vehicle = None
        self.floor_number = floor_number
        self.slot_number = slot_number

class ParkingFloor:
    def __init__(self, floor_number, slots):
        self.floor_number = floor_number
        self.slots = slots

class ParkingLot:
    def __init__(self):
        self.lot_id = "PR1234"
        self.floors = []

    def add_floor(self, floor):
        self.floors.append(floor)

    def find_available_slot(self, vehicle_type):
        for floor in self.floors:
            for slot in floor.slots:
                if slot.slot_type == vehicle_type and slot.is_available:
                    return slot
        return None

    def book_slot(self, vehicle_type, registration_number, color):
        vehicle = Vehicle(vehicle_type, registration_number, color)
        slot = self.find_available_slot(vehicle_type)
        if slot:
            slot.is_available = False
            slot.vehicle = vehicle
            ticket_id = f"{self.lot_id}_{slot.floor_number}_{slot.slot_number}"
            return ticket_id
        else:
            return None
    def unpark_vehicle(self, ticket_id):
        for floor in self.floors:
            for slot in floor.slots:
                if not slot.is_available and ticket_id == f"{self.lot_id}_{floor.floor_number}_{slot.slot_number}":
                    slot.is_available = True
                    vehicle = slot.vehicle
                    slot.vehicle = None
                    return vehicle
        return None
    def get_free_slots_per_floor(self, vehicle_type):
        free_slots_per_floor = {}
        for floor in self.floors:
            count = 0
            for slot in floor.slots:
                if slot.slot_type == vehicle_type and slot.is_available:
                    count += 1
            free_slots_per_floor[floor.floor_number] = count
        return free_slots_per_floor

    def get_all_free_slots_per_floor(self, vehicle_type):
        free_slots_per_floor = {}
        for floor in self.floors:
            slots = []
            for slot in floor.slots:
                if slot.slot_type == vehicle_type and slot.is_available:
                    slots.append(slot.slot_number)
            free_slots_per_floor[floor.floor_number] = slots
        return free_slots_per_floor

    def get_occupied_slots_per_floor(self, vehicle_type):
        occupied_slots_per_floor = {}
        for floor in self.floors:
            slots = []
            for slot in floor.slots:
                if not slot.is_available and slot.slot_type == vehicle_type:
                    slots.append(slot.slot_number)
            occupied_slots_per_floor[floor.floor_number] = slots
        return occupied_slots_per_floor


