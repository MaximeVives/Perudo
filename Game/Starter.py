from Game.Actions import choice_limiter
from Game.Player import Player


def add_players():
    players = []
    # Input nb of players
    nb_players = choice_limiter(2, None, "How many players ?")
    for i in range(1, nb_players + 1):
        players.append(Player(input(f"Player {i} name: ")))
    return players


