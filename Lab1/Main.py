from BestFirstSolver import BestFirstSolver
from BreadthFirstSolver import BreadthFirstSolver
from DepthFirstSolver import DepthFirstSolver
from EightGameNode import EightGameNode
from EightGameSpace import Eight_game_space

## Start the Eight game problem solver with the selected board and problem solver

board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
#board = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
#board = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
#board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
try:
    node = EightGameNode(board)
    node.set_cost(0)
    space = Eight_game_space()
    #solver = BestFirstSolver(space, node)
    #solver = BreadthFirstSolver(space, node)
    solver = DepthFirstSolver(space, node)
    solution = solver.search()
    if not(solution is None):
        print(str(solution))
        print("Cost: " + str(solution.cost))
        print("Visited nodes: " + str(space.get_visited_count()))
    else:
        print("No solution")
except BaseException as err:
    print(err)
