# Les boucles en Python

# Pour
print("Boucle Pour:")
for i in range(0, 5):  # pour i allant de 0 à 5 par pas de 1
    print(f"--> i vaut: {i}")  # je repète l'action 5 fois

print("Boucle Pour - un autre exemple:")
for i in range(1, 5, 2):  # pour i allant de 1 à 5 par pas de 2
    print(f"--> i vaut: {i}")  # je repète l'action 2 fois

# TantQue
print("Boucle TantQue:")
x = 0
while x < 5:
    print(f"--> x vaut: {x}")  # je repète l'action 5 fois
    x += 1
