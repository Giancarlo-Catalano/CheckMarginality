import numpy as np

from CombinatorialProblems.CombinatorialProblem import CombinedCombinatorialProblem
from CombinatorialProblems.combinatorial_problems import RR, Trap, OneMax, Parity
from CombinatorialProblems.detect_marginality_of_combinatorial import detect_marginality_of_combinatorial


def run():
    amalgam_problem = CombinedCombinatorialProblem([RR(4), Trap(4), Parity(4), OneMax(4)], aggregation_func=sum)
    random_samples_quantity = 100
    random_samples = [amalgam_problem.random_solution() for _ in range(random_samples_quantity)]

    marginalities = detect_marginality_of_combinatorial(amalgam_problem, samples_to_test_on=random_samples)
    print(np.array(marginalities * 100, dtype=int))

run()

