from ProblemSolver import ProblemSolver
from Path import Path
import heapq

# A best first version of the general problem solver
# using a priority queue to represent the frontier

class BestFirstSolver(ProblemSolver):

    def __init__(self, problem_space, problem_node):
        super(BestFirstSolver, self).__init__(problem_space, problem_node)
        self.frontier = []

    def initialize_frontier(self):
        path = Path()
        path.add(self.start)
        heapq.heappush(self.frontier, path)
        return self.frontier

    def select_and_remove(self):
        return heapq.heappop(self.frontier)

    def update_frontier(self, path):
        moves = self.space.get_moves(path)
        for move in moves:
            self.frontier.append(move)
