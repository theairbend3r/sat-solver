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
        dpll.run(clauses=sudoku.clauses)


if __name__ == "__main__":
    main()
