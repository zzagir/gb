class Stationery:
    title: str

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    title = 'Ручка начала свою работу'

    def draw(self):
        return self.title


class Pencil(Stationery):
    title = 'Карандаш начал свою работу'

    def draw(self):
        return self.title


class Handle(Stationery):
    title = 'Маркер начал свою работу'

    def draw(self):
        return self.title

defstat = Stationery()
defpen = Pen()
defpencil = Pencil()
defhandle = Handle()

print(f'{defstat.draw()} \n')
print(defpen.draw())
print(defpencil.draw())
print(defhandle.draw())