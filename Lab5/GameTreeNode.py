from GameStatus import GameStatus
import copy


# Representation of Game Tree with alpha beta search function
class GameTreeNode:

    # Max depth of search for the computer players
    MAX_DEPTH = 2

    def __init__(self, game_status):
        self.MAX = False
        self.game_status = game_status
        self.depth = 0
        self.best_move = -1
        self.score = 0
        self.computer_player = None

    def leaf(self):
        if self.game_status.finished():
            return True
        if self.depth >= GameTreeNode.MAX_DEPTH:
            return True
        return False

    def score_leaf(self):
        if self.game_status.finished():
            if self.MAX:
                return self.game_status.current_score()
            else:
                return -1 * self.game_status.current_score()
        else:
            return self.evaluate_game_status(self.game_status)

    def evaluate_game_status(self, game_status):
        val = self.computer_player.evaluate_game_status(game_status)
        if self.MAX:
            return val
        else:
            return -1 * val

    def search(self):
        self.MAX = True
        self.alpha_beta(self, -99999999, 999999999)

    def alpha_beta(self, node, alpha, beta):
        if node.leaf():
            return node.score_leaf()
        children = node.generate_children()
        if node.MAX:
            for i in range(len(children)):
                child = children[i]
                score = self.alpha_beta(child, alpha, beta)
                if score > alpha:
                    alpha = score
                    node.best_move = i
                if alpha >= beta:
                    return beta
            self.score = alpha
            return alpha
        else:
            for i in range(len(children)):
                child = children[i]
                score = self.alpha_beta(child, alpha, beta)
                if score < beta:
                    beta = score
                    node.best_move = i
                if alpha >= beta:
                    return alpha
            self.score = beta
            return beta

    def generate_children(self):
        children = []
        for i in range(len(self.game_status.remaining_candidates)):
            new_game_status = GameStatus(copy.deepcopy(self.game_status))
            new_game_status.to_move.move(new_game_status, i)

            new_node = GameTreeNode(new_game_status)
            new_node.computer_player = copy.deepcopy(self.computer_player)
            new_node.depth = self.depth + 1
            if self.MAX:
                new_node.MAX = False
            else:
                new_node.MAX = True

            children.append(new_node)
        return children











