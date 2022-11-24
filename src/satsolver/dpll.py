import random
import numpy as np
from collections import Counter


class DPLL:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def tautology(self, clauses):
        for clause in clauses:
            for c in clause:
                if c in clause and -c in clause:
                    clauses = clauses.remove(clause)
        return clauses

    def make_lists(self, clauses):
        new_clauses = []
        for set in clauses:
            new_clauses.append(list(set))
        return new_clauses

    def make_positive_lists(self, clauses):
        new_clauses = []
        for set in clauses:
            new_clauses.append(list(set))
        for i in range(len(new_clauses)):
            for j in range(len(new_clauses[i])):
                new_clauses[i][j] = abs(new_clauses[i][j])

        return new_clauses

    def count_occurence_1(self, clauses):
        list_clauses = self.make_lists(clauses)
        maximum_occuring_element = Counter(
            element for sublist in list_clauses for element in sublist
        ).most_common(1)
        return maximum_occuring_element[0][0]

    def count_occurence_2(self, clauses):
        list_clauses = self.make_lists(clauses)
        list_clauses_abs = self.make_positive_lists(clauses)

        maximum_occuring_element = Counter(
            element for sublist in list_clauses_abs for element in sublist
        ).most_common(1)
        int_max_element = int(maximum_occuring_element[0][0])

        neg_count = 0
        pos_count = 0

        for i in range(len(list_clauses)):
            for j in range(len(list_clauses[i])):
                if list_clauses[i][j] == int_max_element:
                    pos_count += 1

                if list_clauses[i][j] == -abs(int_max_element):
                    neg_count += 1

        if neg_count > pos_count:
            return -abs(int_max_element)

        return int_max_element

    def unit_clause(self, clauses):
        unit_clauses = []
        for clause in clauses:
            if len(clause) == 1:
                for c in clause:
                    unit_clauses.append(c)
        return unit_clauses

    def dpll_baseline(self, clauses, assignments={}, old_clauses=np.inf, backtracks=0):

        unit_clauses = self.unit_clause(clauses)

        if len(clauses) == 0:
            return True, assignments, backtracks

        if any([len(c) == 0 for c in clauses]):
            return False, None, backtracks

        if unit_clauses == []:
            for x in random.choice(clauses):
                rand_unit_clause = x
        else:
            rand_unit_clause = unit_clauses[0]

        new_clauses = [c for c in clauses if rand_unit_clause not in c]
        new_clauses = [c.difference({-rand_unit_clause}) for c in new_clauses]
        old_clauses = len(new_clauses)

        sat, vals, backtracks = self.dpll_baseline(
            new_clauses,
            {**assignments, **{rand_unit_clause: rand_unit_clause}},
            old_clauses=old_clauses,
            backtracks=backtracks,
        )
        if sat:
            return sat, vals, backtracks
        new_clauses = [c for c in clauses if -rand_unit_clause not in c]
        new_clauses = [c.difference({rand_unit_clause}) for c in new_clauses]
        if len(new_clauses) > old_clauses:
            backtracks += 1
        old_clauses = len(new_clauses)
        sat, vals, backtracks = self.dpll_baseline(
            new_clauses,
            {**assignments, **{-rand_unit_clause: -rand_unit_clause}},
            old_clauses=old_clauses,
            backtracks=backtracks,
        )
        if sat:
            return sat, vals, backtracks

        return False, None, backtracks

    def dpll_heuristic_1(
        self, clauses, assignments: dict = {}, old_clauses=np.inf, backtracks=0
    ):
        unit_clauses = self.unit_clause(clauses)
        if len(clauses) == 0:
            return True, assignments, backtracks

        if any([len(c) == 0 for c in clauses]):
            return False, None, backtracks

        if unit_clauses == []:
            rand_unit_clause = self.count_occurence_1(clauses)

        else:
            rand_unit_clause = unit_clauses[0]

        if rand_unit_clause < 0:
            new_clauses = [c for c in clauses if -rand_unit_clause not in c]
            new_clauses = [c.difference({rand_unit_clause}) for c in new_clauses]
            if len(new_clauses) > old_clauses:
                backtracks += 1
            old_clauses = len(new_clauses)
            sat, vals, backtracks = self.dpll_heuristic_1(
                new_clauses,
                {**assignments, **{-rand_unit_clause: -rand_unit_clause}},
                old_clauses=old_clauses,
                backtracks=backtracks,
            )
            neg_or_pos = "neg"
        else:
            new_clauses = [c for c in clauses if rand_unit_clause not in c]
            new_clauses = [c.difference({-rand_unit_clause}) for c in new_clauses]
            if len(new_clauses) > old_clauses:
                backtracks += 1
            old_clauses = len(new_clauses)
            sat, vals, backtracks = self.dpll_heuristic_1(
                new_clauses,
                {**assignments, **{rand_unit_clause: rand_unit_clause}},
                old_clauses=old_clauses,
                backtracks=backtracks,
            )
            neg_or_pos = "pos"

        if sat:
            return sat, vals, backtracks

        if neg_or_pos == "neg":
            new_clauses = [c for c in clauses if rand_unit_clause not in c]
            new_clauses = [c.difference({-rand_unit_clause}) for c in new_clauses]
            if len(new_clauses) > old_clauses:
                backtracks += 1
            old_clauses = len(new_clauses)
            sat, vals, backtracks = self.dpll_heuristic_1(
                new_clauses,
                {**assignments, **{rand_unit_clause: rand_unit_clause}},
                old_clauses=old_clauses,
                backtracks=backtracks,
            )
        else:
            new_clauses = [c for c in clauses if -rand_unit_clause not in c]
            new_clauses = [c.difference({rand_unit_clause}) for c in new_clauses]
            if len(new_clauses) > old_clauses:
                backtracks += 1
            old_clauses = len(new_clauses)
            sat, vals, backtracks = self.dpll_heuristic_1(
                new_clauses,
                {**assignments, **{-rand_unit_clause: -rand_unit_clause}},
                old_clauses=old_clauses,
                backtracks=backtracks,
            )
        if sat:
            return sat, vals, backtracks

        return False, None, backtracks

    def dpll_heuristic_2(
        self, clauses, assignments: dict = {}, old_clauses=np.inf, backtracks=0
    ):
        unit_clauses = self.unit_clause(clauses)
        if len(clauses) == 0:
            return True, assignments, backtracks

        if any([len(c) == 0 for c in clauses]):
            return False, None, backtracks

        if unit_clauses == []:
            l = self.count_occurence_2(clauses)

        else:
            l = unit_clauses[0]

        if l < 0:
            new_clauses = [c for c in clauses if -l not in c]
            new_clauses = [c.difference({l}) for c in new_clauses]
            if len(new_clauses) > old_clauses:
                backtracks += 1
            old_clauses = len(new_clauses)
            sat, vals, backtracks = self.dpll_heuristic_2(
                new_clauses,
                {**assignments, **{-l: -l}},
                old_clauses=old_clauses,
                backtracks=backtracks,
            )
            neg_or_pos = "neg"
        else:
            new_clauses = [c for c in clauses if l not in c]
            new_clauses = [c.difference({-l}) for c in new_clauses]
            if len(new_clauses) > old_clauses:
                backtracks += 1
            old_clauses = len(new_clauses)
            sat, vals, backtracks = self.dpll_heuristic_2(
                new_clauses,
                {**assignments, **{l: l}},
                old_clauses=old_clauses,
                backtracks=backtracks,
            )
            neg_or_pos = "pos"

        if sat:
            return sat, vals, backtracks

        if neg_or_pos == "neg":
            new_clauses = [c for c in clauses if l not in c]
            new_clauses = [c.difference({-l}) for c in new_clauses]
            if len(new_clauses) > old_clauses:
                backtracks += 1
            old_clauses = len(new_clauses)
            sat, vals, backtracks = self.dpll_heuristic_2(
                new_clauses,
                {**assignments, **{l: l}},
                old_clauses=old_clauses,
                backtracks=backtracks,
            )
        else:
            new_clauses = [c for c in clauses if -l not in c]
            new_clauses = [c.difference({l}) for c in new_clauses]
            if len(new_clauses) > old_clauses:
                backtracks += 1
            old_clauses = len(new_clauses)
            sat, vals, backtracks = self.dpll_heuristic_2(
                new_clauses,
                {**assignments, **{-l: -l}},
                old_clauses=old_clauses,
                backtracks=backtracks,
            )
        if sat:
            return sat, vals, backtracks

        return False, None, backtracks

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

    def algorithm_to_name(self, algorithm_number: int) -> str:
        a2n = {1: "Baseline", 2: "Heuristic 1", 3: "Heuristic 2"}

        return a2n[algorithm_number]


if __name__ == "__main__":
    from satsolver.suduko import Sudoku

    sudoku = Sudoku(
        raw_sudoku_filepath="./../../data/sudoku_raw/top91.sdk.txt",
        rules_filepath="./../../data/sudoku_rules/sudoku-rules-9x9.txt",
    )

    clauses = sudoku.clauses[0]
    print(len(clauses))
    dpll = DPLL(algorithm=2)
    is_satisfiable, solution_values = dpll.run(clauses=clauses)
    solution = dpll.process_solution(solution_values=solution_values)

    print(f"Sudoku satisfiability = {is_satisfiable}")
    print(f"Solution: \n {solution}")
