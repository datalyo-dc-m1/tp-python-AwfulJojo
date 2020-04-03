# Les tuples

my_tuple = ('a', 'b', 'c', 'd')                     # un tuple d'un seul élément
my_simple_tuple = ('a', )                           # un tuple d'un seul élément
my_tuple_of_tuples = ( ('a', 'b', 'c'), (1, 2, 3))  # un tuple de tuples

length = len(my_tuple)             # taille du tuple

first_elem = my_tuple[0]           # accès au premier élément
last_elem = my_tuple[-1]           # accès au dernier élément
elements = my_tuple[1:3]           # accès aux éléments compris entre 2 indices
first_elems = my_tuple[:3]         # accès aux 3 premiers éléments

count_a = my_tuple.count('a')      # compte le nombre d'occurences

# Concaténer 2 tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenate = tuple1 + tuple2

print(f"Tuple: {my_tuple}")
print(f"Taille: {length}")
print(f"1er élément: {first_elem}")
print(f"Dernier élément: {last_elem}")
print(f"Elements 1 à 3 (exclu): {elements}")
print(f"3 premiers éléments: {first_elems}")
print(f"Nombre de 'a' dans le tuple: {count_a}")
print(f"Concaténation de {tuple1} & {tuple2}:  {concatenate}")
