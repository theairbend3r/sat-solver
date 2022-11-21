import random
from collections import Counter
def experiment_sudoku(filename: str, size: int):
    experiment = []
    sudoku1 = open(filename, "r")
    t = []
    for line in sudoku1:
        temp = []
        for chr in line:
            temp.append(chr)
        t.append(temp)
    size_list = 1

    for line in t:
        for i in range(len(line)):
            print(82 - line.count("."))
            if 82 - line.count(".") <= size and size_list <= 11:
                experiment.append(line)
                size_list += 1
            elif size_list >= 11:
                break
            else:
                try:
                    int(line[i])
                    line[i] = "."
                except ValueError:
                    continue

    return experiment, size
def encode_sudoku(experiment: list, size: int):
    f = open("experiment" + str(size - 1) + ".cnf", 'w')

    for line in experiment:
        index = 0
        f.write("p cnf 999" + "\n")
        for i in range(9):       
            for j in range(9):
                if line[index] != ".":
                    f.write(str(i+1)+str(j+1)+str(line[index]) + " 0"+ "\n")
                index += 1
        f.write("\n")

experiment_1, size = experiment_sudoku("/Users/alonefrati/Desktop/KR-1/top2365.sdk.txt", 16)
encode_sudoku(experiment_1, size)

def get_cnf(filename: str):
    rules = open(filename, "r")
    cnf_list = []
    for line in rules:
        input = line.split()
        if input[0] == "p":
            continue
        cnf_list.append([int(x) for x in input if x!="0"])
    return(cnf_list)

def tautology(cnf):
    for clause in cnf:
        for c in clause:
            if c in clause and -c in clause:
                cnf = cnf.remove(clause)
    return(cnf)

def unit_clause(cnf):
    unit_clauses = []
    for clause in cnf:
        if len(clause) == 1:
            for c in clause:
                unit_clauses.append(c)
    return(unit_clauses)

def dpll(cnf, assignments={}):
    
    unit_clauses = unit_clause(cnf)

    if len(cnf) == 0:
        return True, assignments
 
    if any([len(c)==0 for c in cnf]):
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

# encode_sudoku("top91.sdk.txt")
# rules = get_cnf("sudoku-rules-9x9.txt")
# sudoku = get_cnf("encoded-sudoku-1.cnf")
#
# clause_list =  sudoku + rules
# clause_list = [set(ele) for ele in clause_list]
#
# cnf = tautology(clause_list)
#
# sat, vals = dpll(cnf)
#
# all_solutions = vals.values()
# sudoku_solution = []
# for solution in all_solutions:
#     if solution > 0:
#         sudoku_solution.append(solution)
#
# sudoku_solution.sort()
# print(sudoku_solution)
# print(len(sudoku_solution))
