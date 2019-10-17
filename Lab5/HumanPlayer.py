from Player import Player
import copy


# Class for human player
class HumanPlayer(Player):

    def __init__(self, compatibility_score_set):
        super(HumanPlayer, self).__init__(compatibility_score_set)
        self.name = "You"

    # Lets a player give input to choose candidates
    def make_move(self, game_status):
        accepted = False

        while not accepted:
            answer = input("Choose move (integer) > ")
            try:
                index = int(answer)
            except:
                print(answer, " is not a number")
                continue

            if index < len(game_status.remaining_candidates):
                accepted = True
            else:
                print(answer, " illegal move!")
        self.print_move(game_status, index)
        self.move(game_status, index)

    def copy(self):
        result = copy.deepcopy(self)
        return result
