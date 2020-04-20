# t = [1, 2, 3, 4, 5]
# a = t[0] + t[3]
# b = t[-1]
# c = t[3:]
# a = a + t[-2]
#
#
# abc = ['a', 'b', 'c', 'd', 'e']
# print(abc[3])
# print(abc[-3:])

liste = [1, 4, 1, 2, 1, 5, 3, 1, 12]
a = len(liste)
b = liste[0]
liste.append(0)
c = len(liste)
d = liste[-1]

liste.extend([2, 9, 1])
while liste.count(1) > 0:
    liste.remove(1)
liste.sort()
print(liste)
print("min : ", liste[0], "max : ", liste[len(liste)-1]) #min et max vu que la liste est triée
print(max(liste), min(liste))
print("Somme : ", sum(liste))
liste.append("a")
print("Somme : ", sum(liste)) #On ne peut pas additionner deux types différents