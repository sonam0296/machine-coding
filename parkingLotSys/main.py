import sys
sys.path.append('/Users/sonamjha/sonam_project/python_projects/machine_coding')
from parkingLotSys.parkinglot import ParkingLot, ParkingFloor, ParkingSlot

def main():
    parking_lot = ParkingLot()

    # Create parking floors and slots
    floor1 = ParkingFloor(1, [ParkingSlot("Truck", 1, 1)])
    floor2 = ParkingFloor(2, [ParkingSlot("Bike", 2, 1), ParkingSlot("Bike", 2, 1)])
    floor3 = ParkingFloor(3, [ParkingSlot("Car", 3, 1)])
    parking_lot.add_floor(floor1)
    parking_lot.add_floor(floor2)
    parking_lot.add_floor(floor3)

    while True:
        print("\n== Parking Lot System ==")
        print("1. Park Vehicle")
        print("2. Unpark Vehicle")
        print("3. Free Slots per Floor (Specific Vehicle Type)")
        print("4. All Free Slots per Floor (Specific Vehicle Type)")
        print("5. Occupied Slots per Floor (Specific Vehicle Type)")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_type = input("Enter vehicle type (Car/Bike/Truck): ")
            registration_number = input("Enter registration number: ")
            color = input("Enter color: ")
            ticket_id = parking_lot.book_slot(vehicle_type, registration_number, color)
            if ticket_id:
                print(f"Vehicle parked successfully. Ticket ID: {ticket_id}")
            else:
                print("No available slot for the specified vehicle type.")

        elif choice == "2":
            ticket_id = input("Enter ticket ID: ")
            vehicle = parking_lot.unpark_vehicle(ticket_id)
            if vehicle:
                print(f"Vehicle unparked successfully. Registration Number: {vehicle.registration_number}")
            else:
                print("Invalid ticket ID or vehicle not found.")

        elif choice == "3":
            vehicle_type = input("Enter vehicle type (Car/Bike/Truck): ")
            free_slots_per_floor = parking_lot.get_free_slots_per_floor(vehicle_type)
            for floor_number, count in free_slots_per_floor.items():
                print(f"Floor {floor_number}: {count} free slots")

        elif choice == "4":
            vehicle_type = input("Enter vehicle type (Car/Bike/Truck): ")
            free_slots_per_floor = parking_lot.get_all_free_slots_per_floor(vehicle_type)
            for floor_number, slots in free_slots_per_floor.items():
                print(f"Floor {floor_number}: {slots} free slots")

        elif choice == "5":
            vehicle_type = input("Enter vehicle type (Car/Bike/Truck): ")
            occupied_slots_per_floor = parking_lot.get_occupied_slots_per_floor(vehicle_type)
            for floor_number, slots in occupied_slots_per_floor.items():
                print(f"Floor {floor_number}: {slots} occupied slots")

        elif choice == "0":
            print("Thank you for using the Parking Lot System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
