from ._grid import empties, candidates
from ._types import Step


def next_step(grid):
    """
    Return the next logical step using supported techniques,
    or None if no logical step is available.
    """

    step = naked_single(grid)
    if step:
        return step

    step = hidden_single(grid)
    if step:
        return step

    return None

def naked_single(grid):
    for r, c in empties(grid):
        cand = candidates(grid, r, c)
        if len(cand) == 1:
            v = next(iter(cand))
            return Step(
                row=r,
                col=c,
                value=v,
                technique="Naked single",
                explanation=(
                    f"Cell ({r+1},{c+1}) has only one possible value: {v}."
                ),
            )
    return None

def hidden_single(grid):
    # Rows
    for r in range(9):
        steps = _hidden_in_units([(r, c) for c in range(9)], grid)
        if steps:
            return steps

    # Columns
    for c in range(9):
        steps = _hidden_in_units([(r, c) for r in range(9)], grid)
        if steps:
            return steps

    # 3x3 Boxes
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            cells = [
                (r, c)
                for r in range(br, br + 3)
                for c in range(bc, bc + 3)
            ]
            steps = _hidden_in_units(cells, grid)
            if steps:
                return steps

    return None

def _hidden_in_units(cells, grid):
    locations = {d: [] for d in range(1, 10)}

    for r, c in cells:
        if grid[r][c] is None:
            for v in candidates(grid, r, c):
                locations[v].append((r, c))

    for v, spots in locations.items():
        if len(spots) == 1:
            r, c = spots[0]
            return Step(
                row=r,
                col=c,
                value=v,
                technique="Hidden single",
                explanation=(
                    f"In this unit, {v} can only go in cell ({r+1},{c+1})."
                ),
            )

    return None
