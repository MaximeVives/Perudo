from Game.Enchere import Enchere
from Game.Starter import add_players
from Game.Actions import choice_limiter, encherir, encherir_palifico, dudo, palifico, calza


class Game:
    def __init__(self):
        self.players = add_players()
        self.turn = 0
        self.round = 0
        self.current_player = self.players[self.turn]
        self.previous_call = None

    def __str__(self):
        return "\n".join(
            [f"{player.name}: {', '.join([str(dice) for dice in player.dices])}" for player in self.players])

    def next_turn(self):
        self.turn += 1
        if self.turn >= len(self.players):
            self.turn = 0
            self.round += 1
        self.current_player = self.players[self.turn]

    def next_round(self):
        self.round += 1
        self.turn = 0
        # dices should be reset here
        for player in self.players:
            player.reset_dices()
        self.current_player = self.players[self.turn]

    def ajdust_player_position(self, first_player):
        # this method is used to put the first player at the first position of the list and following players after
        for i in range(len(self.players)):
            if self.players[i] == first_player:
                self.players = self.players[i:] + self.players[:i]
                break

    def play(self):
        # il faut plusieurs while, un pour le tour, un pour le round, un pour la partie
        # le while de la partie s'arrête quand il n'y a plus qu'un joueur
        # le while du round s'arrête quand tout le monde a joué
        # le while du tour s'arrête quand le joueur a fait un dudo ou un calza
        # Il n'y a pas de limit de round, le round se termine sur un dudo ou un calza

        while True:
            hasDudoOrCalza = False
            isFirstPlayer = True
            self.next_round()
            while not hasDudoOrCalza:
                # Afficher l'enchere précédente
                if self.previous_call is not None:
                    print(f"Enchère précédente: {self.previous_call}")

                print(f"C'est au tour de {self.current_player.name}, que veux tu faire ?")
                choice = self.current_player.choice_action(isFirstPlayer)

                match choice:
                    case 1:
                        print("Enchérir")
                        player_enchere = Enchere(self.previous_call)
                        player_enchere.setEnchere()
                        self.previous_call = player_enchere

                    case 2:
                        print("Dudo")
                    case 3:
                        print("Calza")

                self.next_turn()
                isFirstPlayer = False
