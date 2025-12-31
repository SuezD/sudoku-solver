import pytest
from src._grid import Grid, copy
from src.sudoku_solver.solver import (
    next_step,
    naked_or_hidden_single,
    naked_or_hidden_pair,
    pointing_pair,
    box_line_reduction,
)


@pytest.fixture
def empty_grid() -> Grid:
    return [[None] * 9 for _ in range(9)]


class TestNextStep:
    def test_invalid_grid(self, empty_grid):
        grid = copy(empty_grid)
        grid[0][0] = 1
        grid[0][1] = 1

        with pytest.raises(
            ValueError,
            match="Input grid is not a valid sudoku grid"
        ):
            next_step(grid)

    def test_no_logical_step_empty_grid(self, empty_grid):
        step = next_step(empty_grid)
        assert step is None

    # def test_no_logical_step_filled_grid(self):
    #     grid = [
    #         [6, 7, 2, 3, 9, 8, 4, 5, 1],
    #         [8, 1, 9, 4, 7, 5, 2, 6, 3],
    #         [3, 4, 5, None, 6, None, 7, 8, 9],
    #         [1, 3, 7, 5, 8, 9, 6, 2, 4],
    #         [5, 2, 4, 6, 1, 3, 8, 9, 7],
    #         [9, 8, 6, 7, 2, 4, 1, 3, 5],
    #         [4, 9, 8, None, 5, None, 3, 7, 6],
    #         [7, 5, 1, 8, 3, 6, 9, 4, 2],
    #         [2, 6, 3, 9, 4, 7, 5, 1, 8],
    #     ]

    #     step = next_step(grid)
    #     assert step is None

    def test_naked_single_and_hidden_single_precedence(self, empty_grid):
        grid = copy(empty_grid)
        grid[0] = [1, 2, 3, 4, 5, 6, 7, 8, None]
        grid[1][0] = 4
        grid[1][1] = 5
        grid[2][8] = 6

        step = next_step(grid)
        assert step is not None
        assert step.technique == "Naked Single"

    def test_naked_pair_and_hidden_pair_precedence(self, empty_grid):
        grid = copy(empty_grid)
        grid[0] = [1, 2, 3, 4, 5, 6, 7, None, None]
        grid[1][0] = 4
        grid[1][1] = 5
        grid[8][2] = 7
        grid[8][3] = 8

        step = next_step(grid)
        assert step is not None
        assert step.technique == "Naked Pair"

    def test_naked_single_and_hidden_pair_precedence(self, empty_grid):
        grid = copy(empty_grid)
        grid[0] = [1, 2, 3, 4, 5, 6, 7, 8, None]
        grid[1][0] = 4
        grid[1][1] = 5
        grid[8][2] = 7
        grid[8][3] = 8

        step = next_step(grid)
        assert step is not None
        assert step.technique == "Naked Single"


class TestNakedSingle:
    def test_naked_single_row(self, empty_grid):
        grid = copy(empty_grid)
        for r in range(8):
            grid[r][0] = r + 1

        step = naked_or_hidden_single(grid)
        assert step is not None
        assert step.technique == "Naked Single"
        assert step.cells == [(8, 0)]
        assert step.value == 9

        next_step_result = next_step(grid)
        assert next_step_result is not None
        assert next_step_result.technique == "Naked Single"

    def test_naked_single_column(self, empty_grid):
        grid = copy(empty_grid)
        for i in range(8):
            grid[0][i] = i + 1

        step = naked_or_hidden_single(grid)
        assert step is not None
        assert step.technique == "Naked Single"
        assert step.cells == [(0, 8)]
        assert step.value == 9

        next_step_result = next_step(grid)
        assert next_step_result is not None
        assert next_step_result.technique == "Naked Single"

    def test_naked_single_box(self, empty_grid):
        grid = copy(empty_grid)
        for i in range(8):
            grid[i // 3][i % 3] = i + 1

        step = naked_or_hidden_single(grid)
        assert step is not None
        assert step.technique == "Naked Single"
        assert step.cells == [(2, 2)]
        assert step.value == 9

        next_step_result = next_step(grid)
        assert next_step_result is not None
        assert next_step_result.technique == "Naked Single"


class TestNakedPair:
    def test_naked_pair_row(self, empty_grid):
        grid = copy(empty_grid)
        grid[0] = [None, None, 3, 4, 5, 6, 7, 8, 9]

        step = naked_or_hidden_pair(grid)
        assert step is not None
        assert step.technique == "Naked Pair"
        assert step.cells == [(0, 0), (0, 1)]

        next_step_result = next_step(grid)
        assert next_step_result is not None
        assert next_step_result.technique == "Naked Pair"

    def test_naked_pair_column(self, empty_grid):
        grid = copy(empty_grid)
        for r in range(9):
            grid[r][0] = None if r < 2 else r + 1

        step = naked_or_hidden_pair(grid)
        assert step is not None
        assert step.technique == "Naked Pair"
        assert step.cells == [(0, 0), (1, 0)]

        next_step_result = next_step(grid)
        assert next_step_result is not None
        assert next_step_result.technique == "Naked Pair"

    def test_naked_pair_box(self, empty_grid):
        grid = copy(empty_grid)
        grid[0] = [1, None, 3, None, None, None, None, None, None]
        grid[1] = [4, 5, 6, None, None, None, None, None, None]
        grid[2] = [None, 8, 9, None, None, None, None, None, None]

        step = naked_or_hidden_pair(grid)
        assert step is not None
        assert step.technique == "Naked Pair"
        assert step.cells == [(0, 1), (2, 0)]

        next_step_result = next_step(grid)
        assert next_step_result is not None
        assert next_step_result.technique == "Naked Pair"


class TestHiddenPair:
    def test_hidden_pair_in_row(self, empty_grid):
        grid = copy(empty_grid)
        grid[0] = [None, None, 3, 4, 5, None, 7, None, 9]
        grid[1] = [None, None, None, None, None, 2, None, 1, None]
        grid[2] = [None, None, None, None, None, 1, None, 2, None]

        step = naked_or_hidden_pair(grid)
        assert step is not None
        assert step.technique == "Hidden Pair"

        next_step_result = next_step(grid)
        assert next_step_result is not None
        assert next_step_result.technique == "Hidden Pair"

    def test_hidden_pair_in_column(self, empty_grid):
        grid = copy(empty_grid)
        for r in range(9):
            grid[r][0] = None if r in (0, 1, 2, 3) else r + 1
        grid[0][8] = 1
        grid[1][8] = 2
        grid[0][5] = 2
        grid[1][5] = 1

        step = naked_or_hidden_pair(grid)
        assert step is not None
        assert step.technique == "Hidden Pair"

        next_step_result = next_step(grid)
        assert next_step_result is not None
        assert next_step_result.technique == "Hidden Pair"

    def test_hidden_pair_in_box(self, empty_grid):
        grid = copy(empty_grid)
        grid[0] = [None, None, 3, None, None, None, None, None, None]
        grid[1] = [None, None, 6, None, None, None, None, None, None]
        grid[2] = [None, None, 9, None, None, None, None, None, None]
        grid[0][3] = 1
        grid[1][3] = 2
        grid[0][6] = 2
        grid[1][6] = 1

        step = naked_or_hidden_pair(grid)
        assert step is not None
        assert step.technique == "Hidden Pair"

        next_step_result = next_step(grid)
        assert next_step_result is not None
        assert next_step_result.technique == "Hidden Pair"


class TestPointingPair:
    def test_pointing_pair_in_row(self, empty_grid):
        grid = copy(empty_grid)
        grid[0] = [1, 2, 3, None, None, None, None, None, None]
        grid[1] = [None, None, None, None, None, None, None, None, None]
        grid[2] = [7, 8, 9, None, None, None, None, None, None]
        grid[3][0] = 4

        step = pointing_pair(grid)
        assert step is not None
        assert step.technique == "Pointing pair"

        next_step_result = next_step(grid)
        assert next_step_result is not None
        assert next_step_result.technique == "Pointing pair"

    def test_pointing_pair_in_column(self, empty_grid):
        grid = copy(empty_grid)
        for r in range(3):
            grid[r][0] = r + 1
            grid[r][1] = r + 4
            grid[r][2] = r + 7
        grid[0][0] = None
        grid[1][0] = None
        grid[2][0] = None
        grid[2][8] = 1

        step = pointing_pair(grid)
        assert step is not None
        assert step.technique == "Pointing pair"

        next_step_result = next_step(grid)
        assert next_step_result is not None
        assert next_step_result.technique == "Pointing pair"

    def test_pointing_pair_in_box(self, empty_grid):
        grid = copy(empty_grid)
        grid[0] = [1, 2, 3, None, None, None, None, None, None]
        grid[1] = [4, 5, 6, None, None, None, None, None, None]
        grid[2] = [None, None, None, None, None, None, None, None, None]
        grid[0][3] = 7

        step = pointing_pair(grid)
        assert step is not None
        assert step.technique == "Pointing pair"

        next_step_result = next_step(grid)
        assert next_step_result is not None
        assert next_step_result.technique == "Pointing pair"


class TestBoxLineReduction:
    def test_box_line_reduction_row(self, empty_grid):
        grid = copy(empty_grid)
        grid[0] = [None, None, None, 4, 5, 6, 7, 8, 9]

        step = box_line_reduction(grid)
        assert step is not None
        assert step.technique == "Box-Line Reduction"

        next_step_result = next_step(grid)
        assert next_step_result is not None
        assert next_step_result.technique == "Box-Line Reduction"

    def test_box_line_reduction_column(self, empty_grid):
        grid = copy(empty_grid)
        for r in range(9):
            grid[r][0] = None if r < 3 else r + 1

        step = box_line_reduction(grid)
        assert step is not None
        assert step.technique == "Box-Line Reduction"

        next_step_result = next_step(grid)
        assert next_step_result is not None
        assert next_step_result.technique == "Box-Line Reduction"
