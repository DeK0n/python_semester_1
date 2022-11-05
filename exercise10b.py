import random


class Car:
    def __init__(self, id="", mspeed=0, cspeed=0, dist=0) -> None:
        self.id = id
        self.mspeed = mspeed  # maximim speed
        self.cspeed = cspeed  # current spped
        self.dist = dist  # travelled distance
        pass

    def show(self):
        if self.dist == GD_Derby.kilometers:
            print(
                f"Car, ID: {self.id} (max speed: {self.mspeed}) current speed is: {self.cspeed:3.0f}  Travelled distance is: {self.dist} WINNER")
        else:
            print(
                f"Car, ID: {self.id} (max speed: {self.mspeed}) current speed is: {self.cspeed:3.0f}  Travelled distance is: {self.dist}")

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


class Race:
    def __init__(self, name, kilometers, cars_list):
        self.name = name
        self.kilometers = kilometers
        self.cars_list = cars_list

    def hour_passes(self):
        for q in self.cars_list:
            q.accelerate(random.randint(-10, 15))
            q.drive(1)

    def print_status(self):
        for r in self.cars_list:
            r.show()
        print("")

    def race_finished(self):
        winners = 0
        for w in self.cars_list:
            if w.dist >= self.kilometers:
                w.dist = self.kilometers
                winners += 1
        if winners > 0:
            return True
        else:
            return False


cars_list = []
for i in range(10):
    if i < 9:
        cars_list.append(Car("ABC-0"+str(i+1), random.randint(100, 200)))
    if i >= 9:
        cars_list.append(Car("ABC-"+str(i+1), random.randint(100, 200)))

GD_Derby = Race("Grand Demolition Derby", 8000, cars_list)
time = 0
print("--- ---")
print(str(GD_Derby.name)+" have started!")
print("--- ---")
while GD_Derby.race_finished() == False:
    time += 1
    GD_Derby.hour_passes()
    GD_Derby.race_finished()
    if time % 10 == 0:
        print(str(time)+" hours passed: ")
        GD_Derby.print_status()
print("The race have finished after "+str(time)+" hours: ")
GD_Derby.print_status()
