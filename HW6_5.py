class Stationery:
    def __init__(self, title):
        self.title=title
    def draw(self):
        print("Запуск отрисовки")
class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручки")
class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандаша")
class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркера")

a=Pencil('карандащ')
a.draw()