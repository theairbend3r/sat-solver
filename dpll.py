import random
from collections import Counter
def encode_sudoku(filename: str):
    sudoku = open(filename, "r")
    t = []
    for line in sudoku:
        temp = []
        for chr in line:
            temp.append(chr)
        t.append(temp)
    size_3 = 1
    size_6 = 1
    size_10 = 1

    experiment = []
    for line in t:
        length = 82 - line.count(".")
        if length == 18 and size_3 <= 10:
            experiment.append(line)
            size_3 += 1
        elif length == 24 and size_6 <= 10:
            experiment.append(line)
            size_6 += 1
        elif length == 27 and size_10 <= 10:
            experiment.append(line)
            size_10 += 1

    print(size_3, size_6, size_10)
    f = open("experiment.cnf", 'w')

    for line in experiment:
        index = 0
        f.write("p cnf 999" + str(t.index(line)) + "\n")
        for i in range(9):       
            for j in range(9):
                if line[index] != ".":
                    f.write(str(i+1)+str(j+1)+str(line[index]) + " 0"+ "\n")
                index += 1
        f.write("\n")

encode_sudoku("/Users/alonefrati/Desktop/KR-1/top2365.sdk.txt")

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
