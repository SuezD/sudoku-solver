
# Sudoku Solver

A Python library for solving and validating Sudoku puzzles programmatically.


## Features

- Solve standard 9x9 Sudoku puzzles step-by-step
- Validate Sudoku grids
- Check for unique solutions
- Easy to use as a Python library


## Installation

### From PyPI (recommended)

```bash
pip install sudoku-solver
```

### Development install (from source)

```bash
git clone https://github.com/yourusername/sudoku-solver.git
cd sudoku-solver
pip install -r requirements.txt
```

## Usage

Import the library and use its functions in your Python code:

```python
from validator import is_valid, has_one_solution
from solver import next_step

# Example 9x9 Sudoku grid (0 or None for empty cells)
grid = [
	[5, 3, 0, 0, 7, 0, 0, 0, 0],
	[6, 0, 0, 1, 9, 5, 0, 0, 0],
	[0, 9, 8, 0, 0, 0, 0, 6, 0],
	[8, 0, 0, 0, 6, 0, 0, 0, 3],
	[4, 0, 0, 8, 0, 3, 0, 0, 1],
	[7, 0, 0, 0, 2, 0, 0, 0, 6],
	[0, 6, 0, 0, 0, 0, 2, 8, 0],
	[0, 0, 0, 4, 1, 9, 0, 0, 5],
	[0, 0, 0, 0, 8, 0, 0, 7, 9],
]

# Validate the grid
print(is_valid(grid))

# Check for unique solution
print(has_one_solution(grid))

# Get the next logical solving step
step = next_step(grid)
if step:
	print(f"Row: {step.row}, Col: {step.col}, Value: {step.value}")
	print(f"Technique: {step.technique}")
	print(f"Explanation: {step.explanation}")
else:
	print("No further logical steps found.")
```


## Contributing

Pull requests are welcome. Please ensure your code passes all tests and Snyk scans.
