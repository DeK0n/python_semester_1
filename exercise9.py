import random

class Car:
    def __init__(self, id="", mspeed=0, cspeed=0, dist=0) -> None:
        self.id = id
        self.mspeed = mspeed
        self.cspeed = cspeed
        self.dist = dist
        pass

    def show(self):
        print(f"Car, ID: {self.id} (max speed: {self.mspeed}) current speed is: {self.cspeed:3.0f}  Travelled distance is: {self.dist}")

    def accelerate(self, change):
        self.cspeed = self.cspeed + change
        if self.cspeed < 0:
            self.cspeed = 0
        elif self.cspeed > self.mspeed:
            self.cspeed = self.mspeed
        else:
            self.cspeed = self.cspeed

    def travel_time(self, hours):
        self.dist = self.dist + self.cspeed*hours

    def drive(self, hours):
        self.dist += self.cspeed*hours


cars_list = []
for i in range(10):
    cars_list.append(Car("ABC-"+str(i+1), random.randint(100, 200)))

maxDist = 0
while maxDist < 10000:
    for q in cars_list:
        Car.accelerate(q, random.randint(-10, 15))
        Car.drive(q, 1)
        if q.dist > maxDist:
            maxDist = q.dist
        if q.dist > 10000:
            q.dist = 10000
for r in cars_list:
    Car.show(r)    

