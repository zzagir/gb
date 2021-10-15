class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = float(speed)
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала со скоростью {self.speed}")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction: str):
        print(f"Машина {self.name} повернула на сторону {direction}")

    def show_speed(self, max_speed):
        if self.speed >= max_speed:
            return print(f"Вы превышаете скорость! Снизьте скорость до {max_speed}")
        else:
            return print(f"Ваша скорость - {self.speed} не превышает норму")


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class Police(Car):
    pass


town = TownCar('Audi', '59', 'blue', False)
town.go(), town.show_speed(60), town.turn('right'), town.stop()
print("\n")

work = WorkCar('VAZ', '42', 'black', False)
work.go(), work.show_speed(40), work.turn('left'), work.stop()
print("\n")

sport = SportCar('BMW', '115', 'white', False)
sport.go(), sport.turn('left'), sport.stop()
print("\n")

police = Police('Priora', '80', 'Blue', True)
police.go(), police.turn('right'), police.stop()
print("\n")
