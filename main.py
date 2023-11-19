# Excercise 10

#Ex 10.1
class Elevator:
    def __init__(self, bottom_floors, top_floors):
        self.bottom_floors = bottom_floors
        self.top_floors = top_floors
        self.current_floor = bottom_floors

    def floor_up(self):
        if self.current_floor < self.top_floors:
            print(f"The elevator is moving up from {self.current_floor} to {self.current_floor + 1} floor")
            self.current_floor += 1
            return True
        else:
            False

    def floor_down(self):
        if self.current_floor > self.bottom_floors:
            print(f"The elevator is moving down from {self.current_floor} to {self.current_floor - 1} floor")
            self.current_floor -=1
            return True
        else:
            False

    def go_to_floor(self, floor):
        if floor > self.current_floor:
            for i in range(floor - self.current_floor):
                if not self.floor_up():
                    break


        elif floor < self.current_floor:
            for i in range(self.current_floor - floor):
                if not self.floor_down():
                    break

        else:
            print(f"Yor are already in the {self.current_floor}")

# Ex 10.2

class Building:
    def __init__(self,bottom_floors, top_floors, elevator_list):
        self.elevator_list=[]
        for i in range (elevator_list):
            self.elevator_list.append(Elevator(bottom_floors,top_floors))

    def run_elevator(self,elevator_no, floor):
        print()
        print(f"The elevator number {elevator_no} is running")
        self.elevator_list[elevator_no-1].go_to_floor(floor)

#Ex 10.3

    def fire_alarm(self):
        print("--------")
        print("FIREEEEE")
        for i in  self.elevator_list:
            i.go_to_floor(i.bottom_floors)


f = Elevator(1, 7)
f.go_to_floor(6)

b1= Building(1, 7,3)
b1.run_elevator(1, 5)
b1.run_elevator(2,4)


#Ex 10.4

import random
class Car:
    def __init__(self,registration_number,max_speed):
        self.registration_number=registration_number
        self.max_speed=max_speed
        self.current_speed=0
        self.travelled_distance=0

    def accelerate(self, speed):
        self.current_speed += speed
        if self.current_speed >= self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed <= 0:
            self.current_speed = 0

    def drive(self,hours):
        self.travelled_distance += self.current_speed*hours


class Race:
    def __init__(self, name:str, distance:int, car_list:list):
        self.name = name
        self.distance = distance
        self.car_list = car_list
        print(f'{self.name}, distance {self.distance} km, participating cars:')
        for car in self.car_list:
            print(f'{car.registration_number}, max speed {car.max_speed} km/h.')

    def hour_passes(self):
        for car in self.car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"Reg. Number |  Current Speed | Travelled Distance")
        for car in self.car_list:
            print(f"{car.registration_number:^11} | {car.current_speed:^9} km/h |  {car.travelled_distance:^10} km.")

    def race_finished(self):
        max_distance = 0
        for car in self.car_list:
            max_distance = max(max_distance, car.travelled_distance)
        if max_distance >= self.distance:
            return True


car_list = []
for i in range(10):
    car_list.append(Car(f"ABC-{i+1}", random.randint(100, 200)))

race = Race('Grand Demolition Derby', 8000, car_list)
print()

hour = 0
while race.race_finished() is not True:
    hour +=1
    race.hour_passes()
    if hour % 10 == 0:
        print(f'After {hour} hours:')
        race.print_status()
        print()
print(f'The race finished after {hour} hours:')
race.print_status()


