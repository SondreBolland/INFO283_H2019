from Candidate import Candidate
from SelectTeam import SelectTeam
from SimpleComputerPlayer import SimpleComputerPlayer
from SuperComputerPlayer import SuperComputerPlayer
from HyperComputerPlayer import HyperComputerPlayer

super_wins = 0
simple_wins = 0
draws = 0
n_games = 100
for i in range(n_games):
    print("\nGame nr: ", str(i+1))
    Candidate.random_assignment()
    game = SelectTeam()

    # SuperComputer starts every even round
    if i % 2 == 0:
        game.player1 = SuperComputerPlayer(1)
        game.player2 = SimpleComputerPlayer(2)
        game.game_status.to_move = game.player1
        game.game_status.other = game.player2
    else:
        game.player1 = SuperComputerPlayer(2)
        game.player2 = SimpleComputerPlayer(1)
        game.game_status.to_move = game.player2
        game.game_status.other = game.player1

    # Run a game
    while not(game.finished()):
        game.select_move()

    if game.player1.score() > game.player2.score():
        super_wins += 1
    elif game.player1.score() < game.player2.score():
        simple_wins += 1
    else:
        draws += 1

print(game.player1.name + " wins: " + str(super_wins) + "  " + game.player2.name + " wins: " + str(simple_wins) + "  " +
      "Draws: " + str(draws))
