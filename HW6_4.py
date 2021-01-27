import random
class Car:
    def __init__(self, speed, color, name, is_police):
       self.speed =speed
       self.color=color
       self.name=name
       self.is_police=is_police

    def go(self):
        print("Машина поехала")
    def stop(self):
        print("Машина остановилась")
    def turn(self, direction):
        direction =["направо", "налево"]
        a=random.randint(0,1)
        print(direction[a])
    def show_speed(self):
        print(f'Текушая скорость {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        print(f'Текушая скорость {self.speed} км/ч')
        if self.speed >60:
            print("Осторожно! Превышение скорости")


class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        print(f'Текушая скорость {self.speed} км/ч')
        if self.speed > 40:
            print("Осторожно! Превышение скорости")
class Police(Car):
    pass

car = WorkCar(45, "yellow", "Ford", False)
car.show_speed()
