
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.position = bottom

    def floor_up(self):
        if self.position < self.top:
            self.position += 1
            print("Elevator moved to: " + str(self.position))
            return True
        else:
            return False

    def floor_down(self):
        if self.position > self.bottom:
            self.position -= 1
            print("Elevator moved to: " + str(self.position))
            return True
        else:
            return False

    def go_to_floor(self, floor):
        if floor == self.position:
            print("Elevator is already here")
        if floor > self.position:
            while floor > self.position:
                self.floor_up()
        if floor < self.position:
            while floor < self.position:
                self.floor_down()


# h = Elevator(1, 10)
# h.go_to_floor(4)
# h.go_to_floor(1)

# 2

class Building:
    def __init__ (self, bottom, top, elevator_list):
        self.elevator_list = []
        for i in range (elevator_list):
            self.elevator_list.append (Elevator(bottom,top))
    def run_elevator(self, elevator_no, floor):
        print(f"The elevator number {elevator_no} is running")
        self.elevator_list[elevator_no - 1].go_to_floor(floor)
    def fire_alarm(self):
        print("-------")
        print("FIRE!!!")
        number = 0
        for i in self.elevator_list:
            print(f"Elevator {number +1}:")
            number +=1
            i.go_to_floor(i.bottom)

print("Elevators in the building: ")
building = Building(1,7,3)
building.run_elevator(1,4)
building.run_elevator(2,5)
building.run_elevator(3,1)
building.fire_alarm()

