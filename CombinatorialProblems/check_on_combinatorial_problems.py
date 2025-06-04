import numpy as np

from CombinatorialProblems.CombinatorialProblem import CombinedCombinatorialProblem
from CombinatorialProblems.combinatorial_problems import RR, Trap, OneMax, Parity, TwoPeaks, LeadingOnes, \
    SixBitMultiplexer
from CombinatorialProblems.detect_marginality_of_combinatorial import detect_marginality_of_combinatorial


def run():
    sub_problems = [OneMax(4), TwoPeaks(6), RR(4), Trap(4), Parity(4), LeadingOnes(6), SixBitMultiplexer()]
    amalgam_problem = CombinedCombinatorialProblem(sub_problems, aggregation_func=sum)
    random_samples_quantity = 1000
    random_samples = [amalgam_problem.random_solution() for _ in range(random_samples_quantity)]

    cardinality = 2  # they are all binary
    normalisation_denominator = cardinality * (cardinality -1)
    marginalities = detect_marginality_of_combinatorial(amalgam_problem, samples_to_test_on=random_samples) / normalisation_denominator

    current_start = 0
    for sub_problem in sub_problems:
        print(str(type(sub_problem)))
        n_vars = sub_problem.n
        for i in range(current_start, current_start+n_vars):
            print(f"\t var = {i}, marginality = {marginalities[i]:.3f}")
        current_start += n_vars

    print(np.array(marginalities))

run()