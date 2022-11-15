class DPLL:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def dpll_baseline(self, input_file_path):
        print(f"running dpll baseline on file {input_file_path}")

    def dpll_heuristic_1(self, input_file_path):
        print(f"running dpll 1 on file {input_file_path}")

    def dpll_heuristic_2(self, input_file_path):
        print(f"running dpll 2 on file {input_file_path}")

    def run(self, input_file_path):
        if self.algorithm == 1:
            self.dpll_baseline(input_file_path=input_file_path)
        elif self.algorithm == 2:
            self.dpll_heuristic_1(input_file_path=input_file_path)
        elif self.algorithm == 3:
            self.dpll_heuristic_2(input_file_path=input_file_path)
        else:
            raise ValueError("Algorithm does not exist. Use 1, 2 or 3.")
