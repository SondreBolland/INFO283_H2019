from __future__ import division
import math
import random
from InvitationProblem import InvitationProblem
from InvitationAssignment import InvitationAssignment


# This class implements and runs a greedy algorithm and a simulated annealing
# algorithm for maximising an objective function for the problem of who to
# invite to a party given candidates defined in Candidate.py and constraints
# defined in InvitationProblem.py
class InvitationSolver:

    INITIAL_TEMPERATURE = 20.0
    COOLING_FACTOR = 0.95

    def greedy_solve(self):
        best = self.initialize_random()
        best_score = self.score(best)

        while True:
            best_neighbour = self.get_best_neighbour(best)
            best_neighbour_score = self.score(best_neighbour)

            if best_neighbour_score > best_score:
                best = best_neighbour
                best_score = best_neighbour_score
            else:
                break
        return best

    def simulated_annealing_solve(self, cooling_factor):
        best = self.initialize_random()
        best_score = self.score(best)
        temperature = InvitationSolver.INITIAL_TEMPERATURE

        no_improvement = 0
        while no_improvement < 20:
            random_neighbour = self.get_random_neighbour(best)
            random_neighbour_score = self.score(random_neighbour)
            if random_neighbour_score >= best_score:
                best = random_neighbour
                best_score = random_neighbour_score
                no_improvement = 0
            else:
                diff = best_score - random_neighbour_score
                p = math.exp(-diff / temperature)
                x = random.uniform(0, 1)
                if x < p:
                    best = random_neighbour
                    best_score = random_neighbour_score
                    no_improvement = 0
                else:
                    no_improvement += 1
                temperature *= cooling_factor
        return best

    # Computes a random neighbour to an InvitationAssignment
    def get_random_neighbour(self, best):
        size = len(best.the_assignment)
        n = random.randint(0, size-1)
        to_change = InvitationProblem.all_candidates[n]
        result = InvitationAssignment(best)
        result.invert(to_change)
        return result

    # Gets the neighbour that scores highest among the neighbours to an assignment
    def get_best_neighbour(self, best):
        best_new = None
        best_score = -999999999999

        for candidate in best.the_assignment:
            try_assignment = InvitationAssignment(best)
            try_assignment.invert(candidate)

            try_score = self.score(try_assignment)

            if best_new is None or try_score > best_score:
                best_new = try_assignment
                best_score = try_score

        return best_new

    # Scores an assignment
    def score(self, assignment):
        result = self.individual_scores(assignment) + self.constraint_score(assignment)
        return result

    # Computes the individual scores for an assignment
    def individual_scores(self, assignment):
        result = 0.0
        for candidate in assignment.the_assignment:
            if assignment.is_invited(candidate):
                result += candidate.likeability
        return result

    #  Computes the sum of all the constraints in the InvitationProblem on the
    #  particular assignment
    def constraint_score(self, assignment):
        result = InvitationProblem.constraint_score(assignment)
        return result

    # makes a random assignment of invitations
    def initialize_random(self):
        result = InvitationAssignment()
        for candidate in InvitationProblem.all_candidates:
            n = random.randint(0, 1)
            if n == 0:
                result.set(candidate, False)
            else:
                result.set(candidate, True)
        return result


