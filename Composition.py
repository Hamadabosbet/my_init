class Engine:
    def __init__(self, model):
        self.model = model

class Wheels:
    def __init__(self, count):
        self.count = count

class Interior:
    def __init__(self, color):
        self.color = color

class Car:
    def __init__(self):
        self.engine = Engine("V8")
        self.wheels = Wheels(4)
        self.interior = Interior("Leather")


car=Car()