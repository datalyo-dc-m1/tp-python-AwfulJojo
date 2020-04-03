# Déclaration de la classe Phone qui définit une catégorie de téléphones
class Phone:

    """
    Le constructeur avec le mot clé __init__
    Il permet de créer un objet
    C'est ici qu'on définit les attributs
    """
    def __init__(self, constructor, model, color, name, number):
        self.constructor = constructor
        self.model = model
        self.color = color
        self.name = name
        self.number = number

    """
    Les méthodes de la classe
    """
    def turn_on(self):
        print("Je m'allume!")

    def turn_off(self):
        print("Je m'éteins!")

    def print_me(self):
        print(f"Je suis un {self.model} {self.color} de la marque {self.constructor}")

    def call(self, phone):
        print(f"J'appelle le {phone.model} de {phone.name} au {phone.number} depuis {self.model} de {self.name}")


# Construire un objet
iphone_8 = Phone("Apple", "iPhone 8", "rouge", "sarah", "06000000000")

# Appel des méthodes de l'objet
iphone_8.print_me()
iphone_8.turn_on()
iphone_8.turn_off()

# Accès aux attributs de l'objet
color = iphone_8.color
model = iphone_8.model
constructor = iphone_8.constructor

# Appel entre deux téléphones
sarah_iphone = Phone("Apple", "iPhone 8", "rouge", "sarah", "06000000000")
laurent_android = Phone("Android", "S8", "bleu", "laurent", "07000000000")
sarah_iphone.call(laurent_android)
