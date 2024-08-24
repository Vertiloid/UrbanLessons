class Horse:
    def __init__(self, x_distance = 0):
        self.x_distance = x_distance
    sound = 'Frrr'
    def run(self, dx):
        self.x_distance += dx
class Eagle:
    def __init__(self, y_distance = 0):
        self.y_distance = y_distance
    sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy):
        self.y_distance += dy
class Pegasus(Eagle, Horse):
    def __init__(self, x_distance = 0, y_distance = 0):
        self.x_distance = x_distance
        self.y_distance = y_distance
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)
    def get_pos(self):
        return (self.x_distance, self.y_distance)
    def voice(self):
        print(self.sound)


p1 = Pegasus(0, 0)

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()