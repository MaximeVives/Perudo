from Game.Actions import choice_limiter


class Enchere:
    def __init__(self, previous_call=None):
        self.previous_call = previous_call
        self.nb_de = 0
        self.valeur = 0

    def setEnchere(self):
        self.nb_de = choice_limiter(1, 30, "How many dice ?")
        self.valeur = choice_limiter(1, 6, "What value ?")

    def __str__(self):
        return f"Nb de dé :{self.nb_de}, de valeur : {self.valeur}"
