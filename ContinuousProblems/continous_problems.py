import numpy as np

from ContinuousProblems.ContinuousProblem import ContinuousProblem


class RastriginProblem(ContinuousProblem):
    def __init__(self, n, A=10):
        lower_bounds = -5.12 * np.ones(n)
        upper_bounds = 5.12 * np.ones(n)
        self.A = A
        super().__init__(lower_bounds, upper_bounds)

    def fitness_function(self, x):
        return self.A * self.n + np.sum(x**2 - self.A * np.cos(2 * np.pi * x))


class SphereProblem(ContinuousProblem):
    def __init__(self, n):
        lower_bounds = -5.12 * np.ones(n)
        upper_bounds = 5.12 * np.ones(n)
        super().__init__(lower_bounds, upper_bounds)

    def fitness_function(self, x):
        return np.sum(x**2)


class RosenbrockProblem(ContinuousProblem):
    def __init__(self, n, a=1, b=100):
        lower_bounds = -5 * np.ones(n)
        upper_bounds = 10 * np.ones(n)
        self.a = a
        self.b = b
        super().__init__(lower_bounds, upper_bounds)

    def fitness_function(self, x):
        return np.sum(self.b * (x[1:] - x[:-1]**2)**2 + (self.a - x[:-1])**2)


class AckleyProblem(ContinuousProblem):
    def __init__(self, n):
        lower_bounds = -5 * np.ones(n)
        upper_bounds = 5 * np.ones(n)
        super().__init__(lower_bounds, upper_bounds)

    def fitness_function(self, x):
        a = 20
        b = 0.2
        c = 2 * np.pi
        sum_sq = np.sum(x**2)
        sum_cos = np.sum(np.cos(c * x))
        return -a * np.exp(-b * np.sqrt(sum_sq / self.n)) - np.exp(sum_cos / self.n) + a + np.exp(1)


class LinearProblem(ContinuousProblem):
    coeffs: np.ndarray
    def __init__(self, n):
        lower_bounds = np.zeros(n)
        upper_bounds = np.ones(n)

        super().__init__(lower_bounds, upper_bounds)
        self.coeffs = np.arange(n) + 1


    def fitness_function(self, x):
        return np.sum(self.coeffs * x)

