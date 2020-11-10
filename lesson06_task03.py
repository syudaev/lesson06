# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def get_full_name(self):
        return f"{self.name} {self.surname}"


class Position(Worker):

    def get_total_income(self):
        print(
            f'\nWorker: {self.get_full_name()}  Wage: {self._income.setdefault("wage")} '
            f'Bonus: {self._income.setdefault("bonus")} '
            f'Income: {(self._income.setdefault("wage") + self._income.setdefault("bonus"))}')


income_total = Position("Mark", "Guess", "Accountant", {"wage": 20000, "bonus": 5000})
income_total.get_total_income()
