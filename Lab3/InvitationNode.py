from Guest import Guest


# A represention of a node in a CSP search tree for the invitation problem
class InvitationNode:

    def __init__(self):
        self.anne = Guest("Anne", 0)
        self.ola = Guest("Ola", 1)
        self.jan = Guest("Jan", 2)
        self.sondre = Guest("Sondre", 3)
        # TODO
        self.guests = [self.anne, self.ola, self.jan, self.sondre]
        self.assigned_count = 0

    def neighbours(self):
        result = list()
        invitation_node = self.copy_and_add_assignment(True)
        if not(invitation_node is None) and invitation_node.consistent():
            result.append(invitation_node)

        invitation_node = self.copy_and_add_assignment(False)
        if not(invitation_node is None) and invitation_node.consistent():
            result.append(invitation_node)

        return result

    # Makes a new node with assignment for one more guest
    def copy_and_add_assignment(self, is_invited):
        if self.assigned_count == len(self.guests):
            return None

        invitation_node = InvitationNode()
        for i in range(self.assigned_count):
            invitation_node.guests[i].set_invited(self.guests[i].is_invited())
        invitation_node.guests[self.assigned_count].set_invited(is_invited)
        invitation_node.assigned_count = self.assigned_count + 1
        return invitation_node

    # Constraints for the invitation problem
    def consistent(self):
        constraint1 = self.passes_test(not(self.anne.is_invited()) or not(self.ola.is_invited()), self.ola.rank)
        constraint2 = self.passes_test(not(self.anne.is_invited() or self.jan.is_invited()), self.jan.rank)
        # TODO, add constraints here
        return constraint1 and constraint2

    # Checks if an assignment passes a logical test
    # It passes if it is true or if the highest ranked guest has not been assigned yet
    def passes_test(self, bol, max_rank):
        if max_rank < self.assigned_count:
            return bol
        return True

    def all_assigned(self):
        return self.assigned_count == len(self.guests)

    def __str__(self):
        string = "{"
        n_guests = len(self.guests)
        for i in range(len(self.guests)-1):
            guest = self.guests[i]
            if guest.is_invited():
                string += guest.name + ", "
        string += self.guests[(n_guests-1)].name
        string += "}"
        return string

    def __hash__(self):
        result = 0
        for i in range(self.assigned_count):
            if self.guests[i].is_invited():
                result += i
        return result





