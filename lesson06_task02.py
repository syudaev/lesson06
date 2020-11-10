# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода. Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length: int
    _width: int

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def weight_calc_area(self):
        return self._length * self._width


class Calc(Road):
    thickness: int
    weight: int

    def __init__(self, length: int, width: int, thickness: int):
        super().__init__(length, width)
        self.thickness = thickness
        self.weight = 25

    def weight_calc(self):
        return self.weight_calc_area() * self.thickness * self.weight / 1000


weight_road = Calc(5000, 20, 5)
print(f"\n\x1b[34mМасса асфальта, необходимого для покрытия всего дорожного полотна >>>\x1b[0m "
      f"{weight_road.weight_calc():.0f} т")
