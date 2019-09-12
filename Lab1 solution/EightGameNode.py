
# Representation of one state in the game
class EightGameNode:

    def __init__(self, board, cost=1):
        self.default_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.empty_x = 2
        self.empty_y = 2
        self.cost = cost

        if len(board) == 3 and len(board[0]) == 3 and len(board[1]) == 3 and len(board[2]) == 3:
            self.board = board
        else:
            print("Invalid board")
            self.board = self.default_board
        self.initialize_empties()

    # Finds the coordinates of the empty tile and saves them
    def initialize_empties(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    self.empty_x = col
                    self.empty_y = row

    def copy(self):
        new_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                new_board[row][col] = self.board[row][col]
        copy = EightGameNode(new_board, self.cost)
        return copy

    def move_left(self):
        if self.empty_x == 0:
            return None
        else:
            result = self.copy()
            result.board[self.empty_y][self.empty_x] = result.board[self.empty_y][self.empty_x-1]
            result.board[self.empty_y][self.empty_x - 1] = 0
            result.empty_x -= 1
            result.set_cost(1)
            return result

    def move_right(self):
        if self.empty_x == 2:
            return None
        else:
            result = self.copy()
            result.board[self.empty_y][self.empty_x] = result.board[self.empty_y][self.empty_x + 1]
            result.board[self.empty_y][self.empty_x + 1] = 0
            result.empty_x += 1
            result.set_cost(1)
            return result

    def move_up(self):
        if self.empty_y == 0:
            return None
        else:
            result = self.copy()
            result.board[self.empty_y][self.empty_x] = result.board[self.empty_y - 1][self.empty_x]
            result.board[self.empty_y - 1][self.empty_x] = 0
            result.empty_y -= 1
            result.set_cost(1)
            return result

    def move_down(self):
        if self.empty_y == 2:
            return None
        else:
            result = self.copy()
            result.board[self.empty_y][self.empty_x] = result.board[self.empty_y + 1][self.empty_x]
            result.board[self.empty_y + 1][self.empty_x] = 0
            result.empty_y += 1
            result.set_cost(1)
            return result

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

    def print(self):
        for row in self.board:
            print(row)
        print("-----------")

    def __hash__(self):
        sum = 0
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                sum += col * self.board[row][col]
        return sum

