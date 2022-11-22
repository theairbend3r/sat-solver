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

    # csv file to store experiment data for visualization
    with open("./data/output/experiment_stats.csv", "w") as f:
        f.write(
            "run,algorithm,is_satisfiable,sudoku_file,sudoku_file_id,time_elapsed solution"
        )

    # run all algorithms
    runs = 1

    for run in range(1, runs + 1):
        for algorithm in [1, 2, 3]:
            dpll = DPLL(algorithm=algorithm)
            for clauses_idx, clauses in enumerate(sudoku.clauses):
                print(f"Running algorithm {algorithm}.")
                # measure running time of dpll
                start = perf_counter()
                is_satisfiable, solution_values = dpll.run(clauses=clauses)
                end = perf_counter()

                # time elapsed
                time_elapsed = end - start

                # process solution
                solution = dpll.process_solution(solution_values=solution_values)

                # log output
                print(f"DPLL version = {algorithm}")
                print(f"Sudoku satisfiability = {is_satisfiable}")
                print(f"Time elapsed = {time_elapsed}")
                print(f"Solution: \n {solution}")

                print("=" * 50)

                with open("./data/output/experiment_stats.csv", "a") as f:
                    f.write(
                        f"{run},{dpll.algorithm_to_name(algorithm_number=algorithm)},{is_satisfiable},{raw_sudoku_filepath},{clauses_idx},{time_elapsed},{' '.join(solution)}\n"
                    )

                break

    if __name__ == "__main__":
        main()
