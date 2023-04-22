# create class

def encherir(self, previous_call, enchere):
    # This method is a bool that returns True if the player can bid or False if he can't
    # To bid he has to call a higher number of dice or a higher value of dice
    # If the player calls the same number of dice, he has to call a higher value
    # If the player calls the same number of dice and the same value, he can't bid
    # If the player calls a lower number of dice or a lower value of dice, he can't bid
    # If the player calls a lower number of dice and a higher value of dice, he can't bid
    # If the player calls a higher number of dice and a lower value of dice, he can't bid
    # If the value of the dice is 1, the player can call any number of dice with a minimum of previous_call.nb_de / 2 rounded up
    # If the previous call is None, the player can call any number of dice with a minimum of 1 but not the value 1
    # If the previous call nb_de is 1, the player can call an other number of dice if the nb_de is twice + 1 the previous call nb_de
    if previous_call is None:
        if enchere.nb_de > 1 and enchere.valeur > 1:
            return True
        return False
    if enchere.valeur == 1:
        if enchere.nb_de >= previous_call.nb_de / 2:
            return True
        return False
    if enchere.nb_de > previous_call.nb_de:
        return True
    if enchere.nb_de == previous_call.nb_de:
        if enchere.valeur > previous_call.valeur:
            return True
        return False
    if enchere.nb_de < previous_call.nb_de:
        if enchere.valeur > previous_call.valeur:
            if enchere.nb_de == previous_call.nb_de * 2 + 1:
                return True
            return False
        return False
    return False


def encherir_palifico(self, previous_call, enchere):
    # with palifico, the player can call any number of dice with a minimum of 1
    # the first value of the dice has to be the same as the previous call
    if previous_call is None:
        if enchere.nb_de > 1 and enchere.valeur > 1:
            return True
        return False
    if enchere.nb_de > 1:
        return True
    return False


def dudo(self, previous_call, real_value):
    if previous_call.valeur <= real_value:
        return False
    return True

def palifico(self, joueurs):
    for joueur in joueurs:
        if len(joueur.dices) == 1:
            return True
    return False

def calza(self, previous_call, real_value):
    if previous_call == real_value:
        return True
    return False
