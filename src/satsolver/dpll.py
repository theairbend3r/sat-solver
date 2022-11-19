class DPLL:
    def __init__(self, algorithm):
        self.algorithm = algorithm

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
