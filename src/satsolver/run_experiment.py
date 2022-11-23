import datetime
from time import perf_counter

from dpll import DPLL
from suduko import Sudoku
import sys
sys.path.append("/code/sat-solver/src/satsolver/data/")
def main():
    # path wrt to the directory where the program is being called.
    # Assumption: it is being called from the same dir as `sat-solver/`
    # raw_sudoku_filepath = "./data/sudoku_raw/top91.sdk.txt"

    # read rules
    RULES_FILEPATH = "data/sudoku_rules/sudoku-rules-9x9.txt"

    # read sudokus
    RAW_SUDOKU_BASE_FILEPATH = "data/sudoku_raw"
    RAW_SUDOKU_FILENAMES = [
        "experiment_raw4.cnf",
        "experiment_raw9.cnf",
        "experiment_raw15.cnf",
        "experiment_raw18.cnf",
    ]

    # create csv file to store experiment data for visualization
    current_datetime = datetime.datetime.now()
    unique_file_id = f"{current_datetime.year}_{current_datetime.month}_{current_datetime.day}_{current_datetime.hour}_{current_datetime.minute}"

    with open(f"./data/output/experiment_stats_{unique_file_id}.csv", "w") as f:
        f.write(
            "run,algorithm,is_satisfiable,sudoku_file,sudoku_id,backtracks,time_elapsed,solution\n"
        )

    # experiment params
    RUNS = 3
    ALGORITHMS = [1, 2, 3]

    # Loop config:
    # for algorithm in ALGORITHMS:
    #     for raw_sudoku_filename in RAW_SUDOKU_FILENAMES:
    #         for sudoku in sudoku.all_sudoku_clauses:
    #             for run in RUNS:

    # for all runs
    for run in range(1, RUNS + 1):
        print(f"[{run}/{RUNS}] Run.\n")
        # for all algorithms
        for algorithm in ALGORITHMS:
            dpll = DPLL(algorithm=algorithm)
            print(f"\t[{algorithm}/{len(ALGORITHMS)}] Algorithm.\n")

            # for all files that contain multiple sudokus
            for file_idx, raw_sudoku_filename in enumerate(RAW_SUDOKU_FILENAMES):
                raw_sudoku_filepath = (
                    f"{RAW_SUDOKU_BASE_FILEPATH}/{raw_sudoku_filename}"
                )
                sudoku = Sudoku(
                    raw_sudoku_filepath=raw_sudoku_filepath,
                    rules_filepath=RULES_FILEPATH,
                )
                print(
                    f"\t\t[{file_idx}/{len(RAW_SUDOKU_FILENAMES)}] Sudoku File ({raw_sudoku_filename}).\n"
                )

                # for all sudokus in the file
                for sudoku_id, sudoku_clauses in enumerate(sudoku.all_sudoku_clauses):
                    print(
                        f"\t\t\t[{sudoku_id}/{len(sudoku.all_sudoku_clauses)}] Sudoku inside file.\n"
                    )

                    # # for all runss
                    # for run in range(1, RUNS + 1):
                    #     print(f"\t\t\t[{run}/{RUNS}] Run.\n")
                    start = perf_counter()
                    is_satisfiable, solution_values, backtracks = dpll.run(clauses=sudoku_clauses)
                    end = perf_counter()

                    # time elapsed
                    time_elapsed = end - start

                    # process solution
                    solution = dpll.process_solution(solution_values=solution_values)

                    # log output
                    print(f"\t\t\t\tSudoku satisfiability = {is_satisfiable}")
                    print(f"\t\t\t\tTime elapsed = {time_elapsed}")
                    print(f"\t\t\t\tSolution = {solution}")
                    print(f"\t\t\t\tSolution = {backtracks}")

                    # save data for analysis
                    with open(
                        f"./data/output/experiment_stats_{unique_file_id}.csv", "a"
                    ) as f:
                        f.write(
                            f"{run},{dpll.algorithm_to_name(algorithm_number=algorithm)},{is_satisfiable},{raw_sudoku_filename},{sudoku_id},{backtracks},{time_elapsed},{' '.join([str(s) for s in solution])}\n"
                        )
                    print()
        print()
        print("=" * 50)
        print()


if __name__ == "__main__":
    main()
