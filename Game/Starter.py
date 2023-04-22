from Game.Player import Player


def add_players():
    players = []
    # Input nb of players
    nb_players = int(input("How many players? "))
    for i in range(1, nb_players + 1):
        players.append(Player(input(f"Player {i} name: ")))
    return players


