class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        leng = self._length
        wid = self._width
        weig = self.weight
        dep = self.depth
        total = leng * wid * weig * dep / 1000
        return print(f"Масса асфальта:\n{leng} м * {wid} м * {weig} кг * {dep} см = ", total, "т")


r = Road(20, 5000, 25, 5)
r.mass()