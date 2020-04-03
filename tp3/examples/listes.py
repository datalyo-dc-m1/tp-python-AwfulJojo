"""
Les listes
"""

my_list = [5, 1, 7, 9, 5]  # ou list(5, 1, 7, 9, 5)

first_elem = my_list[0]         # premier élément de la liste
first_elem = my_list[-1]        # dernier élément de la liste
element = my_list[1:3]          # éléments compris entre les indices 1 et 3 (exclu)

# Information
length = len(my_list)           # taille de la liste
count_5 = my_list.count(5)      # compte le nombre d'occurences
min_list = min(my_list)         # valeur min
max_list = max(my_list)         # valeur max
has_1 = 1 in my_list            # test si un élément est présent dans une liste

# Manipulation
copied = my_list[:]             # copie d'une liste
copied.append(11)               # ajoute un élément à la fin
copied.insert(1, 2)             # ajoute 2 à la position 1
copied.remove(5)                # supprime le premier 5
copied.pop(0)                   # supprime l'élément en position 0
copied.sort()                   # tri par ordre croissant
sorted_list = sorted(my_list)   # crée une nouvelle liste triée à partir de my_list

print(f"Liste: {my_list}")
print(f"Taille: {length}")
print(f"Nombre de 5 : {count_5}")
print(f"Minimum: {min_list}")
print(f"Maximum: {max_list}")
print(f"La liste contient-elle la valeur 1 ? : {has_1}")
print(f"Liste modifiée: {copied}")
print(f"Liste initiale: {my_list}")
print(f"Liste triée: {sorted_list}")
