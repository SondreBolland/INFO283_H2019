from InvitationSolver import InvitationSolver


sol = InvitationSolver()

greedy_score = 0.0
cooling_80_score = 0.0
cooling_95_score = 0.0
cooling_99_score = 0.0

iterations = 100
for i in range(iterations):
    greedy_solution = sol.greedy_solve()
    greedy_score += sol.score(greedy_solution)

    sim_anneal_solution80 = sol.simulated_annealing_solve(0.8)
    cooling_80_score += sol.score(sim_anneal_solution80)

    sim_anneal_solution95 = sol.simulated_annealing_solve(0.95)
    cooling_95_score += sol.score(sim_anneal_solution95)

    sim_anneal_solution99 = sol.simulated_annealing_solve(0.99)
    cooling_99_score += sol.score(sim_anneal_solution99)

    print("Iteration: " + str(i))

print("Average greedy: " + str(greedy_score / iterations))
print("Average annealing cooling 0.80: " + str(cooling_80_score / iterations))
print("Average annealing cooling 0.95: " + str(cooling_95_score / iterations))
print("Average annealing cooling 0.99: " + str(cooling_99_score / iterations))
