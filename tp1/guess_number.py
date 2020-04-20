from random import randint
number_to_guess = randint(0, 10)
has_won = False
while has_won is False:
    user_propal = int(input("Essayez de deviner le nombre entre 0 et 10 : "))
    while user_propal < 0 or user_propal > 10:
        print("Vous devez entrer un nombre entre 0 et 10 !")
        user_propal = int(input("Essayez de deviner le nombre entre 0 et 10 : "))
    if number_to_guess == user_propal:
        has_won = True
    elif number_to_guess > user_propal:
        print("Le nombre que vous avez saisi est trop petit")
    elif number_to_guess < user_propal:
        print("Le nombre que vous avez saisi est trop grand")
print("Vous avez trouvé le nombre ! C'était bien", number_to_guess)
