from Game.De import De


class Player:
    def __init__(self, name):
        self.name = name
        self.dices = [De() for i in range(5)]

    def remove_last_dice(self):
        self.dices.pop()

    def add_dice(self):
        self.dices.append(De())

