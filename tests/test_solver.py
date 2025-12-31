from src._grid import Grid
from src.solver import next_step

def test_next_step_naked_single():
    grid: Grid = [
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
    step = next_step(grid)
    assert step is not None
    assert step.technique in ["Naked single", "Hidden single"]
    assert 1 <= step.value <= 9
