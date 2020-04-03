# Communiquer avec l'utilisateur

# Afficher un message dans la console

print("hello world!")
print("\n")  # retour à la ligne

# print() prend en paramètre une chaîne de caractère mais on peut utiliser "l'interpolation"
x = 3
y = True
print(f"x vaut: {x} et y vaut: {y}")

# Récupérer une valeur saisie dans la console avec la fonction input()

user_input = input("saisir quelque chose: ")
print(user_input)

# input() renvoie toujours une chaîne de caractères mais on peut transformer son type
user_input_int = int(input("saisir un entier: "))
user_input_float = float(input("saisir un décimal: "))
user_input_bool = bool(input("saisir un booléen: "))
