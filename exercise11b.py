import random


class Car:
    def __init__(self, id="", mspeed=0, cspeed=0, dist=0) -> None:
        self.id = id
        self.mspeed = mspeed  # maximim speed
        self.cspeed = cspeed  # current spped
        self.dist = dist  # travelled distance
        pass

    def drive(self, hours):
        self.dist += self.cspeed*hours

    def print_dist(self):
        print("Kilometers of "+str(self.id)+" is "+str(self.dist)+" km")


class ElectricCar(Car):
    def __init__(self, capacity, id="", mspeed=0, cspeed=0, dist=0,):
        super().__init__(id, mspeed, cspeed, dist)
        self.capacity = capacity


class GasolineCar(Car):
    def __init__(self, volume, id="", mspeed=0, cspeed=0, dist=0,):
        super().__init__(id, mspeed, cspeed, dist)
        self.volume = volume


gCar = GasolineCar(32.3, "ACD-123", 165, random.randint(100, 165))
eCar = ElectricCar(52.5, "ABC-15", 180, random.randint(100, 180))

gCar.drive(3)
gCar.print_dist()
eCar.drive(3)
eCar.print_dist()
