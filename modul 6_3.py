class Horse:

    def __init__(self):
        self.x_distance = 0  # пройденный путь
        self.sound = 'Frrr'  # звук коняшки

    def run(self, dx):  # изменение дистанции, увел x_dist на dx
        self.x_distance += dx


class Eagle:

    def __init__(self):
        self.y_distance = 0  # высота полёта
        self.sound = "I train, eat, sleep, and repeat"  # звук орла

    def fly(self, dy):  # изменение дистанции, увел y_dist на dy
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def __init__(self):
        super().__init__()
        Eagle.__init__(self)

    def move(self, dx, dy):  # запускаются наследованные методы run, fly
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
