import cocoex
import numpy as np

from ContinuousProblems.ContinuousProblem import ContinuousProblem
from ContinuousProblems.detect_marginality_of_continuous import detect_marginality_of_continuous


class ContinuousProblemWrapper(ContinuousProblem):
    original_bbob_problem: cocoex.Problem

    def __init__(self, original_problem: cocoex.Problem):
        super().__init__(original_problem.lower_bounds, original_problem.upper_bounds)
        self.original_bbob_problem = original_problem

    def fitness_function(self, x):
        return self.original_bbob_problem(x)

def run():


    solution_sample_quantity = 100

    suite = cocoex.Suite("bbob", "", "")


    for bbob_problem in suite:
        print(f"Testing on {bbob_problem.name}")
        wrapped_problem =  ContinuousProblemWrapper(bbob_problem)
        solution_samples = [wrapped_problem.random_solution() for _ in range(solution_sample_quantity)]
        marginalities = detect_marginality_of_continuous(wrapped_problem,
                                         solution_samples,
                                         samples_per_CP=12)

        # NOTE: I'm still not sure how to normalise these, but my guess would be marginality / (samples_per_CP  * (samples_per_CP - 1))
        print(np.round(marginalities, 2))


run()
