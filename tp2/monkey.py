class Monkey:

    def __init__(self, name, banana):
        self.name = name
        self.banana = banana

    def eat_banana(self):
        print("Un singe nommé", self.name, "mange une banane de couleur", self.banana.color)


class Banana:

    def __init__(self, color):
        self.color = color


banana_yellow = Banana("jaune")
banana_green = Banana("verte")
pierre = Monkey("Pierre", banana_yellow)
bob = Monkey("Bob", banana_green)

pierre.eat_banana()
bob.eat_banana()

