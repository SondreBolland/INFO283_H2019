from Candidate import Candidate
from SelectTeam import SelectTeam


Candidate.random_assignment()
game = SelectTeam()
game.select_starter()

while not(game.finished()):
    game.print_status()
    game.select_move()

game.print_result()