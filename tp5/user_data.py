import unittest


def get_age_average():
    """
    Retourne la moyenne d'âge des utilisateurs
    :return: int
    """
    return 0


def get_favorite_hobby():
    """
    Retourne le hobbie préféré des utilisateurs
    :return: str
    """
    return ""


def count_movie_lovers():
    """
    Retourne le nombre de personnes qui ont déclaré aimer le cinéma
    :return: int
    """
    return 0


def compute_segmentation():
    """
    Retourne la liste des ids utilisateur ciblés par la campagne publicitaire à venir:
    Les hommes entre 25 et 30 ans(inclus) qui aiment le cinéma
    :return: list d'entiers
    """
    return [0]


class UserDataTest(unittest.TestCase):

    def test_get_age_average(self):
        self.assertEqual(get_age_average(), 26)

    def count_movie_lovers(self):
        self.assertEqual(count_movie_lovers(), 7)

    def test_get_favorite_hobby(self):
        self.assertEqual(get_favorite_hobby(), "gaming")

    def test_compute_segmentation(self):
        self.assertEqual(compute_segmentation(), [5, 8, 9, 10])
