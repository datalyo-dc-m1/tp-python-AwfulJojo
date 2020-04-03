# Les listes

a_list = ["a", "b", "c", "d"]      # une liste

length = len(a_list)               # taille de la liste

first_element = a_list[0]          # premier élément de la liste
second_element = a_list[1]         # deuxième élément de la liste
empty = []                         # un liste vide

print(f"\nListe: {a_list} - taille: {length} - premier élément: {first_element} - second élément: {second_element}")

# Parcours d'une liste
print("\nParcours:")
for element in a_list:
    print(element)

# Ajout d'un élément
print("\nAjout d'un élément:")
print(f"Avant: {a_list}")
a_list += [6]        # ajouter un élément à la fin
a_list.append(7)     # ajouter un élément à la fin
a_list.insert(1, 8)  # insérer un élément en seconde position
print(f"Après: {a_list}")


# Suppression d'un élément
print("\nSuppression d'un élément:")
print(f"Avant: {a_list}")
del a_list[0]       # supprimer le premier élément
print(f"Après: {a_list}")
