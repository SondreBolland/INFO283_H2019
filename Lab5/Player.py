from abc import ABC
import copy


# Abstract class to represent a player in the game, both Human and Computer
class Player(ABC):

    def __init__(self, compatibility_score_set):
        self.chosen = []
        self.compatibility_score_set = compatibility_score_set
        self.name = ""

    def score(self):
        sum = 0
        for candidate in self.chosen:
            sum += candidate.score(self.compatibility_score_set)
        return sum

    def chosen_to_string(self):
        string = ""
        for candidate in self.chosen:
            string += candidate.name
            string += "(" + str(candidate.score(self.compatibility_score_set)) + ") "
        return string

    def move(self, game_status, i):
        candidate = copy.deepcopy(game_status.remaining_candidates.pop(i))
        self.chosen.append(candidate)
        game_status.to_move = game_status.other
        game_status.other = self

    def print_move(self, game_status, index):
        print(str(self.name) + " chose " + str(index) + " " + str(game_status.remaining_candidates[index].name) + "("
              + str(game_status.remaining_candidates[index].score(self.compatibility_score_set)) + ")\n")

    def make_move(self, game_status): pass

    def copy(self): pass


