i = somme = 0
userInput = int(input("Combien des premiers nombres impairs voulez-vous additionner ? : "))
for i in range(1, 2*userInput, 2):
    somme = somme+i
print(somme)

