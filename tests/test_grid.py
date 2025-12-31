import pytest
from src._grid import row, col, box, candidates, empties, copy, Grid


@pytest.fixture
def sample_grid() -> Grid:
    return [
        [5, 3, None, None, 7, None, None, None, None],
        [6, None, None, 1, 9, 5, None, None, None],
        [None, 9, 8, None, None, None, None, 6, None],
        [8, None, None, None, 6, None, None, None, 3],
        [4, None, None, 8, None, 3, None, None, 1],
        [7, None, None, None, 2, None, None, None, 6],
        [None, 6, None, None, None, None, 2, 8, None],
        [None, None, None, 4, 1, 9, None, None, 5],
        [None, None, None, None, 8, None, None, 7, 9],
    ]


def test_row(sample_grid):
    assert row(sample_grid, 0) == [5, 3, None, None, 7, None, None, None, None]


def test_col(sample_grid):
    assert col(sample_grid, 0) == [5, 6, None, 8, 4, 7, None, None, None]


def test_box(sample_grid):
    assert box(sample_grid, 0, 0) == [5, 3, None, 6, None, None, None, 9, 8]


def test_candidates(sample_grid):
    c = candidates(sample_grid, 0, 2)
    assert c == {1, 2, 4}


def test_candidates_col():
    grid: Grid = [[None] * 9 for _ in range(9)]
    for r in range(2, 9):
        grid[r][0] = r + 1
    assert candidates(grid, 0, 0) == {1, 2}
    assert candidates(grid, 1, 0) == {1, 2}


def test_empties(sample_grid):
    empties_list = empties(sample_grid)
    assert (0, 2) in empties_list
    assert (1, 1) in empties_list
    assert (8, 8) not in [
        (r, c) for r, c in empties_list if sample_grid[r][c] is not None
    ]


def test_copy(sample_grid):
    g2 = copy(sample_grid)
    assert g2 == sample_grid
    assert g2 is not sample_grid
    assert g2[0] is not sample_grid[0]
