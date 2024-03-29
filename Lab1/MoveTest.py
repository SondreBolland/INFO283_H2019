from EightGameNode import EightGameNode

# Movement test. See that the movement performed is correct on the board
# See that the zero moves in accordance with the instructions

test_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
node = EightGameNode(test_board)

print(str(node))
print("Move down")
node = node.move_down()
print(str(node))
print("Move Up")
node = node.move_up()
print(str(node))
print("Move Right")
node = node.move_right()
print(str(node))
