
# A class that represent a path in a problem space
class Path:

    def __init__(self):
        # Last node i path
        self.the_last = None
        # Path to last node
        self.path_to_here = None
        # Cost of path
        self.cost = 0

    def __str__(self):
        string = ""
        if self.path_to_here is None:
            string += ""
            # Do nothing
        else:
            string += str(self.path_to_here)
        string += str(self.the_last)
        return string

    def add(self, problem_node):
        self.the_last = problem_node
        self.cost += problem_node.cost

    # Creates and return new path.
    # Path so far + the given node
    def augment(self, node):
        copy = Path()
        copy.the_last = node
        copy.path_to_here = self
        copy.cost = self.cost + node.cost
        return copy

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __eq__(self, other):
        return self.cost == other.cost

    def __ne__(self, other):
        return not self.__eq__(other)