import pytest
from src._grid import Grid
from src.sudoku_solver.validator import is_valid, has_one_solution

@pytest.fixture
def valid_grid() -> Grid:
    return [
        [5, 3, None, None, 7, None, None, None, None],
        [6, None, None, 1, 9, 5, None, None, None],
        [None, 9, 8, None, None, None, None, 6, None],
        [8, None, None, None, 6, None, None, None, 3],
        [4, None, None, 8, None, 3, None, None, 1],
        [7, None, None, None, 2, None, None, None, 6],
        [None, 6, None, None, None, None, 2, 8, None],
        [None, None, None, 4, 1, 9, None, None, 5],
        [None, None, None, None, 8, None, None, 7, 9]
    ]

@pytest.fixture
def invalid_grid(valid_grid) -> Grid:
    g = [row[:] for row in valid_grid]
    g[0][0] = 3
    return g

def test_is_valid(valid_grid, invalid_grid):
    assert is_valid(valid_grid)
    assert not is_valid(invalid_grid)

def test_has_one_solution(valid_grid):
    assert has_one_solution(valid_grid)

def test_has_one_solution_multiple_solutions():
    grid: Grid = [[None]*9 for _ in range(9)]
    assert not has_one_solution(grid)

def test_has_one_solution_no_solution():
    grid = [
        [6, 7, 2, 3, 9, 8, 4, 5, 1],
        [8, 1, 9, 4, 7, 5, 2, 6, 3],
        [3, 4, 5, None, 6, None, 7, 8, 9],
        [1, 3, 7, 5, 8, 9, 6, 2, 4],
        [5, 2, 4, 6, 1, 3, 8, 9, 7],
        [9, 8, 6, 7, 2, 4, 1, 3, 5],
        [4, 9, 8, None, 5, None, 3, 7, 6],
        [7, 5, 1, 8, 3, 6, 9, 4, 2],
        [2, 6, 3, 9, 4, 7, 5, 1, 8],
    ]
    assert not has_one_solution(grid)
