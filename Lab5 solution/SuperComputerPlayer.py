from ComputerPlayer import ComputerPlayer
import copy


class SuperComputerPlayer(ComputerPlayer):

    def __init__(self, compatibility_score_set):
        super(SuperComputerPlayer, self).__init__(compatibility_score_set)
        self.name = "SuperComp"

    def evaluate_game_status(self, game_status):
        super_score = 0
        simple_score = 0
        for c in game_status.to_move.chosen:
            super_score += (c.compatibility1 + c.compatibility2)
        for c in game_status.other.chosen:
            simple_score += (c.compatibility1 + c.compatibility2)

        return super_score - simple_score

    def copy(self):
        result = SuperComputerPlayer(self.compatibility_score_set)
        result.chosen = copy.deepcopy(self.chosen)
        return result
