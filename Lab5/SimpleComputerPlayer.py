from ComputerPlayer import ComputerPlayer
import copy


# Simple AI
# Evaluates the game's current status. This value is used in the alpha beta search to select the best candidate
class SimpleComputerPlayer(ComputerPlayer):

    def __init__(self, compatibility_score_set):
        super(SimpleComputerPlayer, self).__init__(compatibility_score_set)
        self.name = "SimpleComp"

    # Heuristic function to evaluate the current state of the game
    def evaluate_game_status(self, game_status):
        return game_status.to_move.score() - game_status.other.score()

    def copy(self):
        result = SimpleComputerPlayer(self.compatibility_score_set)
        result.chosen = copy.deepcopy(self.chosen)
        return result
