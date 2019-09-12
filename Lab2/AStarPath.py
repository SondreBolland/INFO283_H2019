from Path import Path

#  A class that stores paths in A* search and computes the values needed to order A* star paths.
class AStarPath(Path):

    def __init__(self):
        super(AStarPath, self).__init__()
        self.h_value = 0

    def f(self):
        return self.cost + self.h_value

    def set_h_value(self, h):
        self.h_value = h

    def augment(self, node):
        copy = AStarPath()
        copy.the_last = node
        copy.path_to_here = self
        copy.cost = self.cost + node.cost
        return copy

    def __gt__(self, other):
        if isinstance(other, AStarPath):
            return self.f() > other.f()
        else:
            return 9999999999999

    def __lt__(self, other):
        if isinstance(other, AStarPath):
            return self.f() < other.f()
        else:
            return 9999999999999

    def __eq__(self, other):
        return self.f() == other.f()

    def __ne__(self, other):
        return not self.__eq__(other)
