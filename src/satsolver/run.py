import argparse
from satsolver.dpll import dpll


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-S", help="Algorithm type. Takes values: 1, 2, or 3.", type=int
    )
    parser.add_argument(
        "filename",
        help="Input file with required input clauses (sudoku rules + puzzle).",
        type=str,
    )
    args = parser.parse_args()

    if not args.S:
        print("Using default DPLL.")
        args.S = 1

    dpll(algorithm=args.S, problem_file=args.filename)
