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
data/
├── output
│   └── experiment_stats_2022_11_22_16_50.csv
├── sudoku_dimacs
│   └── top91_sudoku.cnf
├── sudoku_raw
│   ├── experiment_raw15.txt
│   ├── experiment_raw18.txt
│   ├── experiment_raw4.txt
│   ├── experiment_raw9.txt
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

> Note: the file paths inside script are relative to the directory the script is called from. Call scripts from
> inside the `sat-solver` directory.

### Single file runner

The CLI argument format is: `SAT -S {n} {filename}` where `n=1, 2, or 3` denotes the algorithm to be run on `filename`.

```
SAT -S 2 mydir/myfile.txt
```

### Experiment Runner

Runs all algorithms against all input files multiple times.

From inside `sat-sover/`, run:

```
sat-solver$ python src/satsolver/run_experiment.py
```
