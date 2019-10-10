from InvitationSolver import InvitationSolver


sol = InvitationSolver()
# Greedy search
greedy_solution = sol.greedy_solve()
greedy_score = sol.score(greedy_solution)

# Simulated annealing
sim_anneal_solution = sol.simulated_annealing_solve()
annealing_score = sol.score(sim_anneal_solution)

print("Greedy search: " + str(greedy_solution))
print("Greedy score: " + str(greedy_score))

print("\nSimulated annealing search: " + str(sim_anneal_solution))
print("Simulated annealing score: " + str(annealing_score))
