import random


def encode_sudoku(filename: str):
    sudoku = open(filename, "r")
    t = []
    for line in sudoku:
        temp = []
        for chr in line:
            temp.append(chr)
        t.append(temp)

    for line in t:
        index = 0
        f = open("encoded-sudoku-" + str(t.index(line) + 1) + ".cnf", 'w')
        f.write("p cnf 999" + str(t.index(line)) + "\n")
        for i in range(9):
            for j in range(9):
                if line[index] != ".":
                    f.write(str(i + 1) + str(j + 1) + str(line[index]) + " 0" + "\n")
                index += 1


def get_cnf(filename: str):
    rules = open(filename, "r")
    cnf_list = []
    for line in rules:
        input = line.split()
        if input[0] == "p":
            continue
        cnf_list.append([int(x) for x in input if x != "0"])
    return (cnf_list)


def tautology(cnf):
    for clause in cnf:
        for c in clause:
            if c in clause and -c in clause:
                cnf = cnf.remove(clause)
    return (cnf)


def unit_clause(cnf):
    unit_clauses = []
    for clause in cnf:
        if len(clause) == 1:
            for c in clause:
                unit_clauses.append(c)
    return (unit_clauses)


def dpll(cnf, assignments={}):
    unit_clauses = unit_clause(cnf)

    if len(cnf) == 0:
        return True, assignments

    if any([len(c) == 0 for c in cnf]):
        return False, None

    if unit_clauses == []:
        for x in random.choice(cnf):
            l = x
    else:
        l = unit_clauses[0]
    new_cnf = [c for c in cnf if l not in c]
    new_cnf = [c.difference({-l}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: l}})
    if sat:
        return sat, vals
    new_cnf = [c for c in cnf if -l not in c]
    new_cnf = [c.difference({l}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{-l: -l}})
    if sat:
        return sat, vals

    return False, None

def to_cnf(input_file):
    return get_cnf(input_file)

input_file = 'sudoku2.cnf'
clause_list = to_cnf(input_file)
clause_list = [set(ele) for ele in clause_list]

cnf = tautology(clause_list)

sat, vals = dpll(cnf)

all_solutions = vals.values()
print("---------------------")
sudoku_solution = []
for solution in all_solutions:
    if solution > 0:
        sudoku_solution.append(solution)

print(sudoku_solution)
print(len(sudoku_solution))

output_file = input_file[:len(input_file) - 3] + "out"
new_file = open(output_file,'w+')

for variable_assignment in sudoku_solution:
    new_file.write(str(variable_assignment) + "\n")

