import random

# from collections import


class DPLL:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def tautology(self, cnf):
        for clause in cnf:
            for c in clause:
                if c in clause and -c in clause:
                    cnf = cnf.remove(clause)
        return cnf

    def unit_clause(self, cnf):
        unit_clauses = []
        for clause in cnf:
            if len(clause) == 1:
                for c in clause:
                    unit_clauses.append(c)
        return unit_clauses

    def dpll(self, cnf, assignments={}):

        unit_clauses = self.unit_clause(cnf)

        if len(cnf) == 0:
            return True, assignments

        if any([len(c) == 0 for c in cnf]):
            return False, None

        if unit_clauses == []:
            for x in random.choice(cnf):
                rand_unit_clause = x
        else:
            rand_unit_clause = unit_clauses[0]

        new_cnf = [c for c in cnf if rand_unit_clause not in c]
        new_cnf = [c.difference({-rand_unit_clause}) for c in new_cnf]
        sat, vals = self.dpll(
            new_cnf, {**assignments, **{rand_unit_clause: rand_unit_clause}}
        )
        if sat:
            return sat, vals
        new_cnf = [c for c in cnf if -rand_unit_clause not in c]
        new_cnf = [c.difference({rand_unit_clause}) for c in new_cnf]
        sat, vals = self.dpll(
            new_cnf, {**assignments, **{-rand_unit_clause: -rand_unit_clause}}
        )
        if sat:
            return sat, vals

        return False, None

    def dpll_baseline(self, clauses: list, solution: dict = {}):
        # write recursive code here
        print(f"running dpll baseline on combined clauses {clauses}")
        if len(clauses) == 0:
            return True
        if any(c == [] for c in clauses):
            return False

        return solution

    def dpll_heuristic_1(self, clauses, solution: dict = {}):
        # write recursive code here
        print(f"running dpll 1 on combined clauses {clauses}")
        return solution

    def dpll_heuristic_2(self, clauses, solution: dict = {}):
        # write recursive code here
        print(f"running dpll 2 on combined clauses {clauses}")
        return solution

    def run(self, clauses: list):
        if self.algorithm == 1:
            solution = self.dpll_baseline(clauses=clauses)
        elif self.algorithm == 2:
            solution = self.dpll_heuristic_1(clauses=clauses)
        elif self.algorithm == 3:
            solution = self.dpll_heuristic_2(clauses=clauses)
        else:
            raise ValueError("Algorithm does not exist. Use 1, 2 or 3.")

        return solution


if __name__ == "__main__":
    from satsolver.suduko import Sudoku

    sudoku = Sudoku(
        raw_sudoku_filepath="./../../data/sudoku_raw/top91.sdk.txt",
        rules_filepath="./../../data/sudoku_rules/sudoku-rules-9x9.txt",
    )

    dpll = DPLL(algorithm=1)

    sat, vals = dpll.dpll(sudoku.clauses, {})

    all_solutions = vals.values()
    print(all_solutions)
    # sudoku_solution = []
    # for solution in all_solutions:
    #     if solution > 0:
    #         sudoku_solution.append(solution)
    #
    # sudoku_solution.sort()
    # print(sudoku_solution)
    # print(len(sudoku_solution))
    print(sat, vals)
