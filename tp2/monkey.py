class Monkey:

    def __init__(self, name):
        self.name = name

    def eat_banana(self, banana):
        print("Un singe nommé", self.name, "mange une banane de couleur", banana.color)

    def copule(self, parent2, nom_enfant):
        print("Un singe nommé", self.name, "copule avec", parent2.name, "et ils ont un enfant nommé", nom_enfant)

class Banana:

    def __init__(self, color):
        self.color = color

class CoupleDeSinges:

    def __init__(self, maman, papa):
        self.maman = maman
        self.papa = papa

    def reproduit(self, nom_enfant):
        enfant = Monkey(nom_enfant)
        print(self.maman.name, "et", self.papa.name, "reproduisent", enfant.name)

# Pierre mange une banane de couleur jaune
banana_yellow = Banana("jaune")
pierre = Monkey("Pierre")
pierre.eat_banana(banana_yellow)

# Marie mange une banane de couleur verte
marie = Monkey("Marie")
banana_green = Banana("verte")
marie.eat_banana(banana_green)

marie.copule(parent2=pierre, nom_enfant="Robert")

couple = CoupleDeSinges(maman=marie, papa=pierre)
couple.reproduit("Robert")