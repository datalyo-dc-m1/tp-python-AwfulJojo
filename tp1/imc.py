taille_saisie = int(input("Combien mesurez-vous ? (em m) : "))
poids = float(input("Combien pesez-vous ? (em kg) : "))
taille = taille_saisie/100
imc = poids/(taille*taille)
print("Votre IMC est de % 12.2f" % imc)
if imc < 18.5 :
    imcDescription = "Vous êtes en état de maigreur"
elif imc < 24.9:
    imcDescription = "Vous êtes normal"
elif imc < 29.9:
    imcDescription = "Vous êtes en état de surpoids"
elif imc < 40:
    imcDescription = "Vous êtes en état d'obésité"
else:
    imcDescription = "Vous êtes en état d'obésité massive"
print(imcDescription)