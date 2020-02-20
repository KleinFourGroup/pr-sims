import numpy.linalg
import numpy.random

class Position:
    def __init__(self, vec):
        self.ndim = len(vec)
        self.pos = vec

    def __str__(self):
        return "({0})".format(", ".join(map(lambda x: "{0:.2f}".format(x), self.pos)))

    def dist(self, other):
        return numpy.linalg.norm(other.pos - self.pos)

class Person:
    def __init__(self, pos, app):
        self.pos = pos
        self.approval = app

    def __str__(self):
        return "Person({0:.2f}, {1})".format(self.approval, self.pos)

class VoterModel:
    def __init__(self, posMeans, posStds, appStd):
        assert len(posMeans) == len(posStds)
        self.ndim = len(posMeans)
        self.posMeans = posMeans
        self.posStds = posStds
        self.appStd = appStd
        
    def generatePerson(self):
        arr = []
        for i in range(self.ndim):
            mu = self.posMeans[i]
            sigma = self.posStds[i]
            arr.append(numpy.random.normal(mu, sigma))
        pos = Position(arr)
        app = numpy.random.lognormal(0, self.appStd)
        return Person(pos, app)
