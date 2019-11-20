import numpy.linalg.norm

class Position:
    def __init__(self, vec):
        self.ndim = len(vec)
        self.pos = vec

    def dist(self, other):
        return numpy.linalg.norm(other.pos - self.pos)
