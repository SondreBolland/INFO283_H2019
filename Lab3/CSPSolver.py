from abc import ABC, abstractmethod
from InvitationNode import InvitationNode


class CSPSolver(ABC):

    def __init__(self):
        self.frontier = []
        self.visited = set()

    # Initializes search and runs it
    def search(self):
        self.initialize_frontier()
        return self.continue_search()

    # Initialize the search problem. The start node is an InvitationNode with no assignments
    def initialize_frontier(self):
        self.frontier.insert(0, InvitationNode())

    # Continues search in a backtracking manner
    def continue_search(self):
        while len(self.frontier) != 0:
            node = self.frontier.pop(0)
            if self.goal(node):
                return node
            self.update_frontier(node)
        return None

    # Gets the children of a node in the graph and adds them to the frontier stack
    # if they are not visited before. The node is also marked as visited
    def update_frontier(self, node):
        new_nodes = node.neighbours()
        self.visited.add(node)
        for n in new_nodes:
            if not(self.visited.__contains__(n)):
                self.frontier.insert(0, n)

    # decides if a node is a goal node
    def goal(self, node):
        return not(node is None) and node.all_assigned() and node.consistent()

    def set_visited(self, visited):
        self.visited = visited
