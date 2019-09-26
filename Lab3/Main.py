from InvitationSolver import InvitationSolver


solver = InvitationSolver()
search = solver.search()
count = 1

while not(search is None):
    print(str(count) + ". Invited guests: " + str(search))
    search = solver.continue_search()
    count += 1

print("Visited nodes in search: " + str(len(solver.visited)))
