# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

from time import sleep


class TrafficLight:
    color_order: list = ["красный", "желтый", "зеленый"]
    __color: list
    color_time: list

    def __init__(self, color=None, color_time=None):
        if color is None:
            color = ["красный", "желтый", "зеленый"]
        if color_time is None:
            color_time = [7, 2, 5]
        self._Human__color = color
        self.color_time = color_time

    def running(self):
        for i in range(len(self._Human__color)):
            print(f"Сейчас горит {self._Human__color[i]}")
            if self._Human__color[i] == "красный" and self._Human__color[i] == TrafficLight.color_order[i]:
                sleep(self.color_time[1])

            elif self._Human__color[i] == "желтый" and self._Human__color[i] == TrafficLight.color_order[i]:
                sleep(self.color_time[1])
            elif self._Human__color[i] == "зеленый" and self._Human__color[i] == TrafficLight.color_order[i]:
                sleep(self.color_time[1])
            else:
                print("\x1b[31mВнимание! Нарушен порядок режимов!\x1b[0m")
                break


print(f'\n\x1b[34mПереключение между режимами в указанном порядке(красный, желтый, зеленый:)\x1b[0m')
traffic_color = TrafficLight(["красный", "желтый", "зеленый"], [7, 2, 5])
traffic_color.running()

print(f'\n\x1b[34mНарушен порядок режимов, сообщение и завершение скрипта(красный, зеленый , желтый:)\x1b[0m')
traffic_color = TrafficLight(["красный", "зеленый", "желтый"], [7, 2, 5])
traffic_color.running()

print(f'\n\x1b[34mПередан пустой порядок цветов, значения определены по умолчанию(красный, желтый, зеленый:)\x1b[0m')
traffic_color = TrafficLight()
traffic_color.running()
