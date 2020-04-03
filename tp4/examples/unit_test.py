"""
Les tests unitaires
"""

import unittest  # import de la librairie permettant de faire des tests unitaires


# Fonction à tester
def say_hello(name="stranger"):
    return f"Hello {name}"


class SayHelloTest(unittest.TestCase):

    # Liste des tests: le nom du test doit commencer par test_ pour qu'il soit reconnu par PyCharm

    def test_say_hello(self):  # méthode de test de la fonction say_hello
        self.assertEqual(say_hello("world"), "Hello world")
        self.assertEqual(say_hello("Sarah"), "Hello Sarah")
        self.assertEqual(say_hello(), "Hello stranger")
        self.assertEqual(say_hello(3), "Hello 3")

    def test_should_fail(self):  # exemple d'un test qui fail
        self.assertEqual(say_hello("world"), "Hello")

