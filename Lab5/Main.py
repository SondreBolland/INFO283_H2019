from Candidate import Candidate
from SelectTeam import SelectTeam

# Randomly assign compatibility scores to each candidate
Candidate.random_assignment()
game = SelectTeam()
game.select_starter()

# While there are still candidates that have not been selected for a team
# continue to select candidates
while not(game.finished()):
    game.print_status()
    game.select_move()

game.print_result()
