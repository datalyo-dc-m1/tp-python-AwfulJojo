# Les structures conditionnelles en Python

# SI... ALORS...
x = 3
if x > 0:
    print(f"{x} est strictement positif")

# SI... ALORS... SINON...
x = 0
if x > 0:
    print(f"{x} est strictement positif")
else:
    print(f"{x} est négatif ou nul")

# SI... SINON SI...
x = 0
if x > 0:
    print(f"{x} est strictement positif")
elif x == 0:
    print(f"{x} est nul")
else:
    print(f"{x} est strictement négatif")

# SELON
x = 5
if x == 0:           # cas 1
    print("x=0")
elif x == 1:         # cas 2
    print("x=1")
elif x == 1:         # cas 3
    print("x=1")
else:
    print(f"x={x}")  # cas par défaut
