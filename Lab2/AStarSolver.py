from BestFirstSolver import BestFirstSolver
from AStarPath import AStarPath
import heapq

# A* solver
class AStarSolver(BestFirstSolver):

    def __init__(self, space, start):
        super(AStarSolver, self).__init__(space, start)

    def initialize_frontier(self):
        path = AStarPath()
        path.add(self.start)
        heapq.heappush(self.frontier, path)
        return self.frontier

    def select_and_remove(self):
        return heapq.heappop(self.frontier)

    def update_frontier(self, path):
        moves = self.space.get_astar_moves(path)
        for move in moves:
            self.frontier.append(move)
