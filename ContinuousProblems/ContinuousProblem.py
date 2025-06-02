from typing import Iterable

import numpy as np


class ContinuousProblem:
    lower_bounds: np.ndarray
    upper_bounds: np.ndarray

    n: int

    def __init__(self, lower_bounds, upper_bounds):
        assert (len(lower_bounds) == len(upper_bounds))
        self.n = len(lower_bounds)
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds

    def fitness_function(self, x):
        raise NotImplementedError()

    def random_solution(self):
        in_0_1 = np.random.rand(self.n)
        return self.lower_bounds + (self.upper_bounds - self.lower_bounds) * in_0_1


class CombinedContinuousProblem(ContinuousProblem):
    original_problems: tuple[ContinuousProblem, ...]
    starts: np.ndarray

    def __init__(self, original_problems: Iterable[ContinuousProblem]):
        self.original_problems = tuple(original_problems)
        lower_bounds = np.hstack([problem.lower_bounds for problem in self.original_problems])
        upper_bounds = np.hstack([problem.upper_bounds for problem in self.original_problems])
        self.starts = np.cumsum([0] + [problem.n for problem in self.original_problems])
        super().__init__(lower_bounds=lower_bounds, upper_bounds=upper_bounds)
