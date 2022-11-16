class DPLL:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def dpll_baseline(self, clauses):
        print(f"running dpll baseline on combined clauses {clauses}")

    def dpll_heuristic_1(self, clauses):
        print(f"running dpll 1 on combined clauses {clauses}")

    def dpll_heuristic_2(self, clauses):
        print(f"running dpll 2 on combined clauses {clauses}")

    def run(self, clauses, assignments: dict):
        if self.algorithm == 1:
            self.dpll_baseline(clauses=clauses)
        elif self.algorithm == 2:
            self.dpll_heuristic_1(clauses=clauses)
        elif self.algorithm == 3:
            self.dpll_heuristic_2(clauses=clauses)
        else:
            raise ValueError("Algorithm does not exist. Use 1, 2 or 3.")
