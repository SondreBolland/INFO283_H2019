from ProblemSolver import ProblemSolver
from Path import Path

# A depth first implementation of the general solver
# using a stack to represent the frontier

class DepthFirstSolver(ProblemSolver):

    def __init__(self, problem_space, problem_node):
        super(DepthFirstSolver, self).__init__(problem_space, problem_node)
        self.frontier = []

    def initialize_frontier(self):
        path = Path()
        path.add(self.start)
        self.frontier.insert(0, path)
        return self.frontier

    def select_and_remove(self):
        return self.frontier.pop(0)

    def update_frontier(self, path):
        moves = self.space.get_moves(path)
        for move in moves:
            self.frontier.insert(0, move)
