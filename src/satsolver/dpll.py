import random


class DPLL:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def tautology(self, clauses):
        for clause in clauses:
            for c in clause:
                if c in clause and -c in clause:
                    clauses = clauses.remove(clause)
        return clauses

    def unit_clause(self, clauses):
        unit_clauses = []
        for clause in clauses:
            if len(clause) == 1:
                for c in clause:
                    unit_clauses.append(c)
        return unit_clauses

    def dpll_baseline(self, clauses, assignments={}):

        unit_clauses = self.unit_clause(clauses)

        if len(clauses) == 0:
            return True, assignments

        if any([len(c) == 0 for c in clauses]):
            return False, None

        if unit_clauses == []:
            for x in random.choice(clauses):
                rand_unit_clause = x
        else:
            rand_unit_clause = unit_clauses[0]

        new_clauses = [c for c in clauses if rand_unit_clause not in c]
        new_clauses = [c.difference({-rand_unit_clause}) for c in new_clauses]
        sat, vals = self.dpll_baseline(
            new_clauses, {**assignments, **{rand_unit_clause: rand_unit_clause}}
        )
        if sat:
            return sat, vals
        new_clauses = [c for c in clauses if -rand_unit_clause not in c]
        new_clauses = [c.difference({rand_unit_clause}) for c in new_clauses]
        sat, vals = self.dpll_baseline(
            new_clauses, {**assignments, **{-rand_unit_clause: -rand_unit_clause}}
        )
        if sat:
            return sat, vals

        return False, None

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

    def process_solution(self, solution_values):
        solution_values = solution_values.values()

        solution = [sol for sol in solution_values if sol > 0]

        return solution


if __name__ == "__main__":
    from satsolver.suduko import Sudoku

    sudoku = Sudoku(
        raw_sudoku_filepath="./../../data/sudoku_raw/top91.sdk.txt",
        rules_filepath="./../../data/sudoku_rules/sudoku-rules-9x9.txt",
    )

    print(len(sudoku.clauses[0]))
    print(sudoku.clauses[0][:25])
    clauses = [set(s) for s in sudoku.clauses[0]]
    dpll = DPLL(algorithm=1)
    sat, vals = dpll.run(clauses)
    all_solutions = vals.values()

    sudoku_solution = []
    for solution in all_solutions:
        if solution > 0:
            sudoku_solution.append(solution)

    print(sudoku_solution)
    print(len(sudoku_solution))
