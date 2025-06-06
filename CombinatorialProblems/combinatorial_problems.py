import numpy as np

from CombinatorialProblems.CombinatorialProblem import CombinatorialProblem

class LeadingOnes(CombinatorialProblem):
    def __init__(self, n: int):
        cardinalities = np.ones(n, dtype=int) * 2
        super().__init__(cardinalities)

    def fitness_function(self, x):
        for index, value in enumerate(x):
            if value == 0:
                return float(index)
        return float(self.n)


class SixBitMultiplexer(CombinatorialProblem):
    def __init__(self):
        super().__init__(np.ones(6, dtype=int) * 2)

    def fitness_function(self, x):
        position = 2*x[0]+x[1]
        return x[position + 2]


class UnitaryProblem(CombinatorialProblem):

    def __init__(self, n: int):
        cardinalities = np.ones(n, dtype=int) * 2
        super().__init__(cardinalities)

    def unitary_function(self, ones):
        raise NotImplementedError()

    def fitness_function(self, x):
        return self.unitary_function(np.sum(x))




class RR(UnitaryProblem):
    def unitary_function(self, ones):
        return float(self.n) if ones == self.n else 0.0


class Trap(UnitaryProblem):
    def unitary_function(self, ones):
        return self.n if ones == self.n else self.n - 1 - ones


class TwoPeaks(UnitaryProblem):
    def unitary_function(self, ones):
        return max(ones, self.n - ones)


class Parity(UnitaryProblem):
    def unitary_function(self, ones):
        return float(ones % 2) * self.n


class OneMax(UnitaryProblem):
    def unitary_function(self, ones):
        return ones


