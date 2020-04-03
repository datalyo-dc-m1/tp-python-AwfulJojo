import unittest

class Fonctions:
    def   Fonction (self, var ):
            if type (var) != int :
                return f"{var} {fonction()}"
            elif    var <= -1  :
             return f"Il est {var} heure "
            elif  var >= 25:
                   return f"{var} nest pas 1 chiffre"
            else:
                if var < 12:
                 return f"Il est {var}HOO, c'est le matin"
                else:
                 if var >= 18:
                  return f"Il est {var}H00, c'est le soir"
                 elif var > 12 and var <= 18 :
                      return f"Il est {var}h, c'est l'après-midi "
                 else     :
                  return f"{var} {fonction()}"

def fonction():
    return "n'est pas un chiffre"
int = 3

print(Fonctions().Fonction(3))

class UnitTest(unittest.TestCase):
    def test_Fonction(self):
        self.assertEqual(Fonctions().Fonction(1), 2)
        self.assertEqual(Fonctions().Fonction(0), 1)
        self.assertEqual(Fonctions().Fonction(-1), 0)
