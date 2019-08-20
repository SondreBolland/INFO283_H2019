from EightGameNode import EightGameNode

# Movement test. See that the movement performed is correct on the board
# See that the zero moves in accordance with the instructions

test_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
node = EightGameNode(test_board)

node.print()
print("Move down")
node = node.move_down()
node.print()
print("Move Up")
node = node.move_up()
node.print()
print("Move Right")
node = node.move_right()
node.print()
