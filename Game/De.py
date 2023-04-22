# create class Dé
import random


class De:
    def __init__(self):
        self.valeur = None
        self.lancer()

    def lancer(self):
        self.valeur = random.randint(1, 6)

    def __str__(self):
        return str(self.valeur)
