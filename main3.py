class Worker:

    def __init__(self, name='Петр', surname='Иванов', position='Администратор', wage=100, bonus=20):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


v_pet = Position('Василий', 'Птичкин', 'танцор', 110, 30)
print(f'Новые атрибуты: {v_pet.name}, {v_pet.surname}, {v_pet.position}, {v_pet._income}')
print(f'Общий доход: {v_pet.get_full_name()} - {v_pet.get_full_salary()}')
