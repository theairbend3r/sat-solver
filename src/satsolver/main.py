import argparse
from time import perf_counter
from satsolver.dpll import DPLL
from satsolver.suduko import Sudoku


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-S", help="Algorithm type. Takes values: 1, 2, or 3.", type=int
    )
    parser.add_argument(
        "raw_input_file_path",
        help="Input file with required input clauses (sudoku rules + puzzle).",
        type=str,
    )
    args = parser.parse_args()

    if not args.S:
        print("Using default DPLL.")
        args.S = 1

    sudoku = Sudoku(
        raw_sudoku_filepath=args.raw_input_file_path,
        # path wrt to the directory where the program is being called.
        # Assumption: it is being called from the same dir as `sat-solver/`
        rules_filepath="./data/sudoku_rules/sudoku-rules-9x9.txt",
    )

    # get clauses for a single sudoku
    clauses = sudoku.all_sudoku_clauses[0]

    # run dpll
    dpll = DPLL(algorithm=args.S)

    # measure running time of dpll
    start = perf_counter()
    is_satisfiable, solution_values, backtracks = dpll.run(clauses=clauses)
    end = perf_counter()

    # process solution
    solution = dpll.process_solution(solution_values=solution_values)

    print(f"DPLL version = {args.S}")
    print(f"Sudoku satisfiability = {is_satisfiable}")
    print(f"Time elapsed = {end - start}")
    print(f"Number of backtracks = {backtracks}")
    print(f"Solution: \n {solution}")


if __name__ == "__main__":
    main()
