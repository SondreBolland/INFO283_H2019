from Player import Player
from GameTreeNode import GameTreeNode


# Abstract class representing a computer
class ComputerPlayer(Player):

    def __init__(self, compatibility_score_set):
        super(ComputerPlayer, self).__init__(compatibility_score_set)
        self.name = "Comp"

    # Finds the best possible candidate to select and selects him
    def make_move(self, game_status):
        selected_candidate_idx = self.select_candidate(game_status)
        self.move(game_status, selected_candidate_idx)

    # Does a alpha beta search to find best candidate to select
    def select_candidate(self, game_status):
        root = GameTreeNode(game_status)
        root.computer_player = self
        root.search()

        return root.best_move

    def evaluate_game_status(self, game_status): pass

