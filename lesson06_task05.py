# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print(f"\nЗапуск отрисовки\n")


class Pen(Stationery):
    def draw(self):
        print(f"Лучше всего получается запуск отрисовки, если в руках {self.title} ")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} тоже неплохой инструмент для запуска отрисовки")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title} весьма непредсказуем для запуска и выполнения отрисовки")


sketch_stationery = Stationery("")
sketch_pen = Pen("Карандаш")
sketch_pencil = Pencil("Ручка")
sketch_handle = Handle("Маркер")

sketch_stationery.draw()
sketch_pen.draw()
sketch_pencil.draw()
sketch_handle.draw()
