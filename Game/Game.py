from Game.Starter import add_players


class Game:
    def __init__(self):
        self.players = add_players()
        self.turn = 0
        self.round = 0
        self.current_player = self.players[self.turn]

    def __str__(self):
        return "\n".join([f"{player.name}: {', '.join([str(dice) for dice in player.dices])}" for player in self.players])
