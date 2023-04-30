from Game.De import De
from Game.Actions import choice_limiter


class Player:
    def __init__(self, name):
        self.name = name
        self.dices = [De() for i in range(5)]
        self.previous_action = None

    def remove_last_dice(self):
        self.dices.pop()

    def add_dice(self):
        self.dices.append(De())

    def reset_dices(self):
        for dice in self.dices:
            dice.lancer()

    def choice_action(self, isFirstPlayer):
        if isFirstPlayer:
            print("1 - Enchérir")
            choice = choice_limiter(1, 1)
        else:
            print("1 - Enchérir")
            print("2 - Dudo")
            print("3 - Calza")
            choice = choice_limiter(1, 3)

        self.previous_action = choice
        return choice