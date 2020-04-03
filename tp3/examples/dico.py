"""
Les dictionnaires
"""

dico = {"prenom": "Toto", "age": 6}  # création d'un dictionnaire

prenom = dico.get("prenom")  # accès à la valeur d'une clé

keys = dico.keys()           # liste des clés contenues dans dico
values = dico.values()       # liste des valeurs contenues dans dico

dico["est_sage"] = True                   # ajoute une nouvelle entrée
dico["est_sage"] = False                  # modifie la valeur d'une clé ou dico.update("est_sage", False)
dico.update({"age": 5, "nom": "Mobile"})  # ajoute de nouvelles entrées ou les modifie si elles existent
dico.pop("prenom")                        # supprime l'entrée associée à la clé

new_dico = dico.copy()     # crée une copie

# Parcours d'un dictionnaire
print("\nParcours du dictionnaire:")
for k, v in dico.items():
    print(k, v)

print("\nParcours des valeurs:")
for v in dico.values():
    print(v)

print("\nParcours des clés:")
for k in dico.keys():
    print(k)


print("\n")
print(f"Dictionnaire modifié: {dico}")
print(f"Valeur de prenom: {prenom}")
print(f"Liste des clés: {keys}")
print(f"Liste des valeurs: {values}")
