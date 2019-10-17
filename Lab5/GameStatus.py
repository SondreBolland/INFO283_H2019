import copy
from Candidate import Candidate


# Class for representing the status of the game
class GameStatus:

    def __init__(self, game_status=None):
        if not(game_status is None):
            self.to_move = game_status.to_move.copy()
            self.other = game_status.other.copy()
            self.remaining_candidates = copy.deepcopy(game_status.remaining_candidates)
        else:
            self.to_move = None
            self.other = None
            self.remaining_candidates = copy.deepcopy(Candidate.candidates)

    def finished(self):
        return len(self.remaining_candidates) <= 0

    def remaining_compatibility(self, player):
        sum = 0
        if player.compatibility_score_set == 1:
            for c in self.remaining_candidates:
                sum += c.compatibility1
        elif player.compatibility_score_set == 2:
            for c in self.remaining_candidates:
                sum += c.compatibility2
        return sum

    def current_score(self):
        return self.to_move.score() - self.other.score()

    def remaining_to_string(self):
        string = ""
        string += "Remaining players to choose from\n"
        string += "      \t\tCompatibility\n"
        string += "No\tCand.\t"+ str(self.to_move.name) + "\t" + str(self.other.name) + "\n"
        for i in range(len(self.remaining_candidates)):
            c = self.remaining_candidates[i]
            if self.to_move.compatibility_score_set == 1:
                to_move_comp = c.compatibility1
                other_comp = c.compatibility2
            else:
                to_move_comp = c.compatibility2
                other_comp = c.compatibility1
            string += str(i) + "\t" + str(c.name) + "\t" + str(to_move_comp) + "\t" + str(other_comp) + "\n"

        string += "\tSum\t" + str(self.remaining_compatibility(self.to_move)) + "\t" + str(self.remaining_compatibility(self.other))
        return string

    def move(self, i):
        self.to_move.move(self, i)

