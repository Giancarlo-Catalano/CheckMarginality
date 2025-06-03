import numpy as np

from ContinuousProblems.ContinuousProblem import ContinuousProblem
from ContinuousProblems.continous_problems import RastriginProblem, SphereProblem, RosenbrockProblem, AckleyProblem, \
    LinearProblem
from ContinuousProblems.detect_marginality_of_continuous import detect_marginality_of_continuous


class CustomContinuousProblem(ContinuousProblem):


    def __init__(self):
        self.n = 10
        super().__init__(np.zeros(10), np.ones(10))

    def fitness_function(self, x):
        return np.prod(x-0.5)


def run():


    solution_sample_quantity = 100
    dimensions = 10
    benchmark_problems = [
        RastriginProblem(n=dimensions),
        SphereProblem(n=dimensions),
        RosenbrockProblem(n=dimensions),
        AckleyProblem(n=dimensions),
        LinearProblem(n=dimensions),
        CustomContinuousProblem()
    ]

    for problem in benchmark_problems:
        solution_samples = [problem.random_solution() for _ in range(solution_sample_quantity)]
        marginalities = detect_marginality_of_continuous(problem,
                                         solution_samples,
                                         samples_per_CP=12)

        print(np.round(marginalities, 2))


run()



