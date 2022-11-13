# sat-solver

## Installation

Create virtual environment (Python=3.10+ recommended).

### Clone repository

```
https://github.com/theairbend3r/sat-solver.git
```

### Create data directory

```
sat-solver/data/
├── sudoku_dimacs
│   └── sudoku1.cnf
├── sudoku_raw
│   └── top91.sdk.txt
└── sudoku_rules
    └── sudoku-rules-9x9.txt
```

### Install local package

Navigate inside `sat-solver` and install package in editable mode.

```
cd sat-solver
pip install -e .
```

### Run file

The CLI argument format is: `SAT -S {n} {filename}` where `n=1, 2, or 3` denotes the algorithm to be run on `filename`.

```
SAT -S 2 mydir/myfile.txt
```
