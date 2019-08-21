from abc import ABC, abstractmethod

class ProblemSolver(ABC):

    def __init__(self, space, start):
        # A representation of the problem space
        self.space = space
        #A representation of the starting position
        self.start = start
        # List of all paths to be searched
        self.frontier = None

    @abstractmethod
    def initialize_frontier(self): pass

    @abstractmethod
    def select_and_remove(self): pass

    @abstractmethod
    def update_frontier(self, path): pass

    #Searches the problem space.
    #Returns path if path to goal is found. Return null if no path to goal
    def search(self):
        frontier = self.initialize_frontier()
        n_nodes = 0
        while len(frontier) != 0:
            path = self.select_and_remove()
            is_goal = self.space.goal(path.the_last)
            if is_goal:
                return path
            self.update_frontier(path)

            if n_nodes % 1000 == 0 and n_nodes != 0:
                print("Nodes searched: " + str(n_nodes))
            n_nodes += 1
        return None

