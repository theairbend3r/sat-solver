import argparse
from satsolver.dpll import DPLL


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-S", help="Algorithm type. Takes values: 1, 2, or 3.", type=int
    )
    parser.add_argument(
        "input_file_path",
        help="Input file with required input clauses (sudoku rules + puzzle).",
        type=str,
    )
    args = parser.parse_args()

    if not args.S:
        print("Using default DPLL.")
        args.S = 1

    dpll = DPLL(algorithm=args.S)
    dpll.run(input_file_path=args.input_file_path)


if __name__ == "__main__":
    main()
