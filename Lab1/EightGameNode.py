
# Representation of one state in the game
class EightGameNode:

    def __init__(self, board, cost=1):
        self.default_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.cost = cost

        if len(board) == 3 and len(board[0]) == 3 and len(board[1]) == 3 and len(board[2]) == 3:
            self.board = board
        else:
            print("Invalid board")
            self.board = self.default_board

    def copy(self):
        new_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                new_board[row][col] = self.board[row][col]
        copy = EightGameNode(new_board, self.cost)
        return copy

    def move_left(self):
        # TODO
        return None

    def move_right(self):
        # TODO
        return None

    def move_up(self):
        # TODO
        return None

    def move_down(self):
        # TODO
        return None

    def __eq__(self, other):
        if isinstance(other, EightGameNode):
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if self.board[col][row] != other.board[col][row]:
                        return False
            return True
        return False

    def equals(self, other_board):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[col][row] != other_board[col][row]:
                    return False
        return True

    def set_cost(self, new_cost):
        self.cost = new_cost

    def __str__(self):
        string = ""
        for row in self.board:
            string += str(row) + "\n"
        string += "----------\n"
        return string

    def __hash__(self):
        sum = 0
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                sum += col * self.board[row][col]
        return sum

