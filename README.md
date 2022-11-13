# sat-solver

## Installation

1. Create virtual environment (Python=3.10+ recommended).

2. Clone repository.

```
https://github.com/theairbend3r/sat-solver.git
```

3. Navigate inside `sat-solver` and install package in editable mode.

```
cd sat-solver
pip install -e .
```

4. Run file. The CLI argument format is: `SAT -S {n} {filename}` where `n=1, 2, or 3`
   denotes the algorithm to be run on `filename`.

```
SAT -S 2 mydir/myfile.txt
```
