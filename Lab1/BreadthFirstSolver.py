from ProblemSolver import Problem_solver
from Path import Path
from collections import deque

# A breadth first solver implementation of the general problem solver
# using a queue to represent frontier

class BreadthFirstSolver(Problem_solver):

    def __init__(self, problem_space, problem_node):
        super(BreadthFirstSolver, self).__init__(problem_space, problem_node)
        self.frontier = []

    def initialize_frontier(self):
        path = Path()
        path.add(self.start)
        self.frontier.insert(0, path)
        return self.frontier

    def select_and_remove(self):
        return self.frontier.pop()

    def update_frontier(self, path):
        moves = self.space.get_moves(path)
        for move in moves:
            self.frontier.insert(0, move)
