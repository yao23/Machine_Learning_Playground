import random

vehicle_sizes = ["Motorcycle", "Compact", "Large"]


class ParkingSpot:
    def __init__(self, level, row, spot_num, spot_size):
        self.level = level
        self.row = row
        self.spot_number = spot_num
        self.spot_size = spot_size
        self.vehicle = None

    def is_available(self):
        return not self.vehicle

    def can_fit_vehicle(self, vehicle):
        """
        :param vehicle:
        :return:

        Checks if the spot is big enough for the vehicle( and is available).This compares the SIZE only.
        It does not check if it has enough spots.
        """
        return self.is_available() and vehicle.can_fit_in_spot(self)

    def park(self, vehicle):
        """
        Park vehicle in this spot.

        :param vehicle:
        :return:
        """
        if not self.can_fit_vehicle(vehicle):
            return False

        self.vehicle = vehicle
        self.vehicle.park_in_spot(self)
        return True

    def get_row(self):
            return self.row

    def get_spot_number(self):
        return self.spot_number

    def get_size(self):
        return self.spot_size

    def remove_vehicle(self):
        """
        Remove vehicle from spot, and notify level that a new spot is available
        :return:
        """
        self.level.spot_freed()
        self.vehicle = None

    def print_parking_spot(self):
        if self.vehicle:
            self.vehicle.print_vehicle()
        else:
            if self.spot_size == vehicle_sizes[1]:  # Compact
                print("c")
            elif self.spot_size == vehicle_sizes[2]:  # Large
                print("l")
            elif self.spot_size == vehicle_sizes[0]:  # Motorcycle
                print("m")


class Level:
    """
    Represents a level in a parking garage
    """
    def __init__(self, floor, num_spots):
        self.__available_spots = 0
        self.__spots_per_row = 10
        self.__floor = floor
        self.__spots = [None] * num_spots
        large_spots = num_spots / 4
        bike_spots = num_spots / 4
        compact_spots = num_spots - large_spots - bike_spots
        for i in range(num_spots):
            vehicle_size = vehicle_sizes[0]  # Motorcycle
            if i < large_spots:
                vehicle_size = vehicle_sizes[2]  # Large
            elif i < large_spots + compact_spots:
                vehicle_size = vehicle_sizes[1]  # Compact
            else:
                pass
            row = i / self.__spots_per_row
            self.__spots[i] = ParkingSpot(self, row, i, vehicle_size)
        self.__available_spots = num_spots

    def available_spots(self):
        return self.__available_spots

    def find_available_spots(self, vehicle):
        """
        find a spot to park this vehicle. Return index of spot, or -1 on failure.

        :param vehicle:
        :return:
        """
        spots_needed = vehicle.get_spots_needed()
        last_row = -1
        spots_found = 0
        for i in range(len(self.__spots)):
            spot = self.__spots[i]
            if last_row != spot.get_row():
                spots_found = 0
                last_row = spot.get_row()
            elif spot.can_fit_vehicle(vehicle):
                spots_found += 1
            else:
                spots_found = 0
            if spots_found == spots_needed:
                return i - (spots_needed - 1)
            else:
                return -1

    def park_starting_at_spot(self, spot_num, vehicle):
        """
        Park a vehicle starting at the spot spotNumber, and continuing until vehicle.spotsNeeded.

        :param spot_num:
        :param vehicle:
        :return:
        """
        vehicle.clear_spots()
        success = True
        for i in range(spot_num, spot_num + vehicle.get_spots_needed() + 1):
            success &= self.__spots[i].park(vehicle)
        self.__available_spots -= vehicle.get_spots_needed()
        return success

    def park_vehicle(self, vehicle):
        """
        Try to find a place to park this vehicle. Return false if failed.

        :param vehicle:
        :return:
        """
        if self.available_spots() < vehicle.get_spots_needed():
            return False
        spot_num = self.find_available_spots(vehicle)
        if spot_num < 0:
            return False
        else:
            return self.park_starting_at_spot(spot_num, vehicle)

    def spot_freed(self):
        """
        When a car was removed from the spot, increment availableSpots

        :return:
        """
        self.__available_spots += 1

    def print_level(self):
        last_row = -1
        for i in range(len(self.__spots)):
            spot = self.__spots[i]
            if spot.get_row() != last_row:
                print(" ")
                last_row = spot.get_row()
            spot.print_parking_spot()


class ParkingLot:
    def __init__(self):
        self.__num_levels = 5
        self.__levels = [None] * self.__num_levels
        for i in range(self.__num_levels):
            self.__levels[i] = Level(i, 30)

    def park_vehicle(self, vehicle):
        for i in range(len(self.__levels)):
            if self.__levels[i].park_vehicle(vehicle):
                return True
        return False

    def print_parking_lot(self):
        for i in range(len(self.__levels)):
            print("Level %d:" % i)
            self.__levels[i].print_level()
            print("")
        print("")


class Vehicle:
    def __init__(self):
        self.parking_spots = []
        self.license_plate = ""
        self.spots_needed = 0
        self.vehicle_sizes = vehicle_sizes[1]

    def get_spots_needed(self):
        return self.spots_needed

    def get_size(self):
        return self.vehicle_sizes

    def park_in_spot(self, spot):
        """
        Park vehicle in this spot (among others, potentially)

        :param spot:
        :return:
        """
        self.parking_spots.append(spot)

    def clear_spots(self):
        """
        Remove car from spot, and notify spot that it's gone

        :return:
        """
        for i in range(len(self.parking_spots)):
            self.parking_spots[i].remove_vehicle()
        del self.parking_spots[:]

    def can_fit_in_spot(self, spot):
        pass

    def print_vehicle(self):
        pass


class Bus(Vehicle):
    """
    Bus
    """
    def __init__(self):
        super(Bus, self).__init__()
        self.spots_needed = 5
        self.size = vehicle_sizes[2]  # Large

    def can_fit_in_spot(self, spot):
        return spot.get_size() == vehicle_sizes[2]

    def print_bus(self):
        print("B")


class Car(Vehicle):
    """
    Bus
    """
    def __init__(self):
        super(Car, self).__init__()
        self.spots_needed = 1
        self.size = vehicle_sizes[1]  # Compact

    def can_fit_in_spot(self, spot):
        return spot.get_size() == vehicle_sizes[2] or spot.get_size() == vehicle_sizes[1]  # Large or Compact

    def print_car(self):
        print("C")


class MotorCycle(Vehicle):
    """
    Bus
    """
    def __init__(self):
        super(MotorCycle, self).__init__()
        self.spots_needed = 1
        self.size = vehicle_sizes[0]  # Motorcycle

    def can_fit_in_spot(self, spot):
        return True

    def print_motorcycle(self):
        print("M")


class ParkingSystem:
    """
    Parking System
    """
    def __init__(self):
        lot = ParkingLot()
        vehicle = None

        while not vehicle or lot.park_vehicle(vehicle):
            lot.print_parking_lot()
            r = random.randint(1, 10)
            if r < 2:
                vehicle = Bus()
            elif r < 4:
                vehicle = MotorCycle()
            else:
                vehicle = Car()
            print("Parking a %s" % vehicle.print_vehicle())

        print("Parking Failed. Final state: %s" % lot.print_parking_lot())
