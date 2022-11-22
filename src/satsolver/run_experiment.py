from time import perf_counter

from satsolver.dpll import DPLL
from satsolver.suduko import Sudoku


def main():
    # path wrt to the directory where the program is being called.
    # Assumption: it is being called from the same dir as `sat-solver/`
    raw_sudoku_filepath = "./data/sudoku_raw/top91.sdk.txt"
    rules_filepath = "./data/sudoku_rules/sudoku-rules-9x9.txt"

    # load suduko
    sudoku = Sudoku(
        raw_sudoku_filepath=raw_sudoku_filepath,
        rules_filepath=rules_filepath,
    )

    # run all algorithms
    for algorithm in [1, 2, 3]:
        dpll = DPLL(algorithm=algorithm)
        for clauses in sudoku.clauses:
            # measure running time of dpll
            start = perf_counter()
            is_satisfiable, solution_values = dpll.run(clauses=clauses)
            end = perf_counter()

            # process solution
            solution = dpll.process_solution(solution_values=solution_values)

            print(f"DPLL version = {algorithm}")
            print(f"Sudoku satisfiability = {is_satisfiable}")
            print(f"Time elapsed = {end - start}")
            print(f"Solution: \n {solution}")

            print("=" * 50)


if __name__ == "__main__":
    main()
