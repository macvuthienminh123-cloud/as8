
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.floor = bottom

    def floor_up(self):
        if self.floor < self.top:
            self.floor = self.floor + 1
            print("Current floor:", self.floor)

    def floor_down(self):
        if self.floor > self.bottom:
            self.floor = self.floor - 1
            print("Current floor:", self.floor)

    def go_to_floor(self, target):
        if target > self.floor:
            while self.floor != target:
                self.floor_up()
        else:
            while self.floor != target:
                self.floor_down()



e = Elevator(1, 10)

e.go_to_floor(4)
e.go_to_floor(2)

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print("Floor:", self.current)

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print("Floor:", self.current)

    def go_to_floor(self, target):
        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()


class Building:
    def __init__(self, bottom, top, num):
        self.elevators = []

        for i in range(num):
            e = Elevator(bottom, top)
            self.elevators.append(e)

    def run_elevator(self, number, target):
        if number >= 0 and number < len(self.elevators):
            print("Elevator", number, "moving to", target)
            self.elevators[number].go_to_floor(target)
        else:
            print("Wrong elevator number")



b = Building(1, 10, 3)

b.run_elevator(0, 5)
b.run_elevator(1, 8)
b.run_elevator(2, 3)

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print("Floor:", self.current)

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print("Floor:", self.current)

    def go_to_floor(self, target):
        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()


class Building:
    def __init__(self, bottom, top, num):
        self.bottom = bottom
        self.elevators = []

        for i in range(num):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, number, target):
        if number >= 0 and number < len(self.elevators):
            print("Elevator", number, "moving to", target)
            self.elevators[number].go_to_floor(target)

    def fire_alarm(self):
        print("Fire alarm! All elevators go down")

        for e in self.elevators:
e.go_to_floor(self.bottom)



b = Building(1, 10, 3)

b.run_elevator(0, 6)
b.run_elevator(1, 8)


b.fire_alarm()

import random

class Car:
    def __init__(self, reg, max_speed):
        self.reg = reg
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def drive(self, hours):
        self.distance = self.distance + self.speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.speed = car.speed + change

            if car.speed < 0:
                car.speed = 0
            if car.speed > car.max_speed:
                car.speed = car.max_speed

            car.drive(1)

    def print_status(self):
        print("Race:", self.name)
        print("Reg   Speed   Distance")

        for car in self.cars:
            print(car.reg, car.speed, car.distance)

        print()

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False



cars = []

for i in range(10):
    reg = "ABC-" + str(i+1)
    max_speed = random.randint(100, 200)
    cars.append(Car(reg, max_speed))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
    race.hour_passes()
    hours = hours + 1

    if hours % 10 == 0:
        race.print_status()


race.print_status()
print("Race finished in", hours, "hours")