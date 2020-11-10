# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    name: str
    color: str
    speed: int
    is_police: bool

    def __init__(self, name: str, color: str, speed: int, is_police: bool, status: str):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self.status = status

    def go(self):
        if self.status == "движется прямо":
            print(f"\nАвтомобиль {self.name}({self.color}) {self.status} ")

    def stop(self):
        if self.status == "остановился":
            print(f"\nАвтомобиль {self.name}({self.color}) {self.status} ")

    def turn(self):
        if self.status == "повернул налево" or self.status == "повернул направо" or self.status == "развернулся":
            print(f"\nАвтомобиль {self.name}({self.color}) {self.status} ")

    def show_speed(self):
        if self.speed != 0:
            print(f"  >>> текущая скорость {self.name}({self.color}) составляет {self.speed} км/ч")


class TownCar(Car):
    max_speed: int
    type_car: str

    def __init__(self, name: str, color: str, speed: int, is_police: bool, status: str, type_car: str, speed_max: int):
        super().__init__(name, color, speed, is_police, status)
        self.max_speed = speed_max
        self.type_car = type_car

    def show_speed(self):
        if self.speed > self.max_speed and self.type_car == "Town Car":
            print(f"  >>> На {self.name} превышена скорость, max разрешенная скорость для {self.type_car} "
                  f"{self.max_speed} км/ч")


class SportCar(Car):
    car_type: str

    def __init__(self, name: str, color: str, speed: int, is_police: bool, status: str, car_type: str):
        super().__init__(name, color, speed, is_police, status)
        self.car_type = car_type

    def car_sport(self):
        if self.car_type == "Sport Car":
            print(f"  >>> {self.name} - это спортивный автомобиль")


class WorkCar(Car):
    max_speed: int
    type_car: str

    def __init__(self, name: str, color: str, speed: int, is_police: bool, status: str, type_car: str, speed_max: int):
        super().__init__(name, color, speed, is_police, status)
        self.max_speed = speed_max
        self.type_car = type_car

    def show_speed(self):
        if self.speed > self.max_speed and self.type_car == "Work Car":
            print(f"  >>> На {self.name} превышена скорость, max разрешенная скорость для {self.type_car} "
                  f"{self.max_speed} км/ч")


class PoliceCar(Car):

    def car_police(self):
        if self.is_police:
            print(f"  >>> {self.name} - это полицейский автомобиль")


car_name = [{"Volvo": ["Black", 110, False, "движется прямо", "Town Car", 60]},
            {"Volkswagen": ["Green", 0, True, "остановился", "Special service car", 110]},
            {"Renault": ["Brown", 55, False, "повернул налево", "Work Car", 50]},
            {"Cherokee": ["Gray", 90, False, "повернул направо", "Four-wheel drive car", 110]},
            {"Toyota": ["White", 100, True, "развернулся", "Special service car", 130]},
            {"Ferrari": ["Red", 220, False, "движется прямо", "Sport Car", 250]}]

car_obj, car_police, car_sport, car_work, car_town = '', '', '', '', ''

for i in range(len(car_name)):
    for key, value in car_name[i].items():
        car_obj = Car(key, value[0], value[1], value[2], value[3])
        car_police = PoliceCar(key, value[0], value[1], value[2], value[3])
        car_sport = SportCar(key, value[0], value[1], value[2], value[3], value[4])
        car_work = WorkCar(key, value[0], value[1], value[2], value[3], value[4], value[5])
        car_town = TownCar(key, value[0], value[1], value[2], value[3], value[4], value[5])
    car_obj.go()
    car_obj.stop()
    car_obj.turn()
    car_obj.show_speed()
    car_work.show_speed()
    car_town.show_speed()
    car_sport.car_sport()
    car_police.car_police()
