class Monkey:

    def __init__(self, name):
        self.name = name

    def eat_banana(self, banana):
        print("Un singe nommé", self.name, "mange une banane de couleur", banana.color)


class Banana:

    def __init__(self, color):
        self.color = color


banana_yellow = Banana("jaune")
banana_green = Banana("verte")
pierre = Monkey("Pierre")
bob = Monkey("Bob")

pierre.eat_banana(banana_yellow)
bob.eat_banana(banana_green)
