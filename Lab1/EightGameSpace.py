from EightGameNode import EightGameNode

# ProblemSolver is an abstract class that defines a generic search
# algorithm for classical AI problem solving
class Eight_game_space:

    def __init__(self):
        self.goal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.goal_node = EightGameNode(self.goal_board)
        # Set of visited nodes
        self.visited = set()

    # Return true if node is goal node
    def goal(self, node):
        if isinstance(node, EightGameNode):
            return node.equals(self.goal_board)
        else:
            return False

    # Performs moves from current state and adds new nodes to the frontier
    def get_moves(self, path):
        result = list()
        last = path.the_last
        if not(self.is_visited(last)):
            move = last.move_left()
            result = self.add_move(path, result, move)

            move = last.move_right()
            result = self.add_move(path, result, move)

            move = last.move_up()
            result = self.add_move(path, result, move)

            move = last.move_down()
            result = self.add_move(path, result, move)

            self.visited.add(last)
        return result

    # If move is legal and the node is not visited, add to path
    def add_move(self, path, result, node):
        if not(node is None) and not(self.is_visited(node)):
            new_path = path.augment(node)
            result.append(new_path)
        return result

    def is_visited(self, node):
        return self.visited.__contains__(node)

    def get_visited_count(self):
        return self.visited.__sizeof__()