import pytest
from src._grid import Grid
from src.validator import is_valid, has_one_solution

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
