

# A class representing information about a potential guest in the invitation CSP
class Guest:

    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.invited = False

    def is_invited(self):
        return self.invited

    def set_invited(self, bol):
        self.invited = bol
