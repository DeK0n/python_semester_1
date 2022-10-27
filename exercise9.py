import random

# 1
# Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled distance.
# Add a class initializer that sets the first two of the properties based on parameter values. The current speed and travelle
# distance of a new car must be automatically set to zero. Write a main program where you create a new car
# (registration number ABC-123, maximum speed 142 km/h). Finally, print out all the properties of the new car.

# 2
# Extend the program by adding an accerelate method into the new class. The method should receive the change of speed (km/h)
# as a parameter. If the change is negative, the car reduces speed. The method must change the value of the speed property
# of the object. The speed of the car must stay below the set maximum and cannot be less than zero. Extend the main program
# so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h. Then print out
# the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the speed and
# then print out the final speed. The travelled distance does not have to be updated yet.

# 3
# Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
# Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5)
# increases the travelled distance to 2090 km.

# class Car:
#     def __init__(self, id = "", mspeed = 0, cspeed = 0, dist = 0) -> None:
#         self.id = id
#         self.mspeed = mspeed
#         self.cspeed = cspeed
#         self.dist = dist
#         pass
#     def show(self):
#         print(f"Car, ID: {self.id} has maximum speed: {self.mspeed} and current speed is: {self.cspeed:3.0f}  Travelled distance is: {self.dist}")
#     def accelerate(self, change):
#         self.cspeed = self.cspeed + change
#         if self.cspeed < 0:
#             self.cspeed = 0
#         elif self.cspeed > self.mspeed:
#             self.cspeed = self.mspeed
#         else:
#             self.cspeed = self.cspeed
#     def travel_time(self, hours):
#         self.dist = self.dist + self.cspeed*hours

# NewCar = Car("ABC-123", 142)
# Car.show(NewCar)
# Car.accelerate(NewCar, 30)
# Car.show(NewCar)
# Car.accelerate(NewCar, 70)
# Car.show(NewCar)
# Car.accelerate(NewCar, 50)
# Car.show(NewCar)
# Car.travel_time(NewCar, 6)
# Car.show(NewCar)
# Car.accelerate(NewCar, -200)
# Car.show(NewCar)

# 4
# Now we will program a car race. The travelled distance of a new car is initialized as zero.
# At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
# The maximum speed of each new car is a random value between 100 km/h and 200 km/h. The registration numbers
# are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins. One per every hour of the race,
# the following operations are performed:

# a)The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
# This is done using the accerelate method.
# b)Each car is made to drive for one hour. This is done with the drive method.


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


# travMAx = 0
# # while travMAx < 10000:
# for t in cars_list:
#     x = random.randint(-10, 15)
#     Car.accelerate(t, x)
#     Car.drive(t, 1)



# 5
# The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each
# car are printed out formatted into a clear table
