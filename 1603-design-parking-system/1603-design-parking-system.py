class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = [0, 0, 0]
        self.limit = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        index = carType - 1
        if self.parking[index] < self.limit[index]:
            self.parking[index] += 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)