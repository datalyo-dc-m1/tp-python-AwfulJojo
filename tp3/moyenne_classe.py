grades = [8, 12, 15, 6, 10, 19, 18, 7, 13, 15, 8, 15, 17, 13, 12, 15, 16, 9, 10, 3, 19, 20, 15]

# Afficher l'écart entre le max et le min de la liste grades
ecart = max(grades)-min(grades)
print(ecart)

# Cette liste correspond en fait aux notes des élèves à un DS de maths:
#Afficher le nombre d'élèves
nb_eleve = len(grades)
print(nb_eleve)

#Un élève était absent, il a rattrapé le controle et obtenu la note de 14. Rajouter cette note à la liste des notes.
grades.append(14)

# Il y a eu une faute de frappe sur la cinquième note. L'élève a eu en réalité 13. Modifier sa note.
grades[4] = 13
print(grades)

# Quelle est la moyenne de la classe?
somme_notes = sum(grades)
moyenne = somme_notes/nb_eleve
print("% 12.2f" % moyenne)

# (Bonus) Quelle est la médiane de la classe?
grades.sort()

# (Bonus) Un élève doit obtenir une note supérieure ou égale à 10 pour valider la matière. Combien de personnes ont validé la matière?

# (Bonus) Un élève qui a obtenu entre 8 et 10 peut effectuer une session de rattrapage. Combien de personnes peuvent aller aux rattrapages? Combien de personnes ont échoué (note strictement inférieure à 8)?