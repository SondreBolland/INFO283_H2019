import random


# Representation of a person to be picked.
# A candidate has a compatibility score for team 1 and a compatibility score for team 2
class Candidate:

    def __init__(self, name):
        self.name = name
        self.compatibility1 = 0
        self.compatibility2 = 0

    def score(self, n):
        if n == 1:
            return self.compatibility1
        elif n == 2:
            return self.compatibility2
        else:
            return -1

    @staticmethod
    def random_assignment():
        sum1 = 0
        sum2 = 0

        for c in Candidate.candidates:
            c.compatibility1 = random.randint(1, 9)
            sum1 += c.compatibility1
            c.compatibility2 = random.randint(1, 9)
            sum2 += c.compatibility2

        while sum1 < 100:
            sum1 = Candidate.add_point1(1, sum1)
        while sum1 > 100:
            sum1 = Candidate.add_point1(-1, sum1)

        while sum2 < 100:
            sum2 = Candidate.add_point2(1, sum2)
        while sum2 > 100:
            sum2 = Candidate.add_point2(-1, sum2)

    @staticmethod
    def add_point1(inc, sum):
        i = random.randint(0, len(Candidate.candidates)-1)
        val = Candidate.candidates[i].compatibility1+inc
        if val < 1 or val > 9:
            return sum
        else:
            Candidate.candidates[i].compatibility1 = val
            return sum+inc

    @staticmethod
    def add_point2(inc, sum):
        i = random.randint(0, len(Candidate.candidates)-1)
        val = Candidate.candidates[i].compatibility2 + inc
        if val < 1 or val > 9:
            return sum
        else:
            Candidate.candidates[i].compatibility2 = val
            return sum + inc


# All candidates
per = Candidate("Per ")
anne = Candidate("Anne")
jonas = Candidate("Jonas")
aud = Candidate("Aud ")
mons = Candidate("Mons")
kari = Candidate("Kari")
roar = Candidate("Roar")
emma = Candidate("Emma")
ola = Candidate("Ola ")
lise = Candidate("Lise")
ivar = Candidate("Ivar")
britt = Candidate("Britt")
dag = Candidate("Dag ")
siri = Candidate("Siri")
tom = Candidate("Tom ")
eli = Candidate("Eli ")
lars = Candidate("Lars")
mia = Candidate("Mia ")
erik = Candidate("Erik")
nora = Candidate("Nora")
helg = Candidate("Helg")
ruth = Candidate("Ruth")

Candidate.candidates = [per, anne, jonas, aud, mons, kari, roar, emma, ola, lise, ivar, britt, dag, siri, tom, eli, lars, mia, erik, nora, helg, ruth]



