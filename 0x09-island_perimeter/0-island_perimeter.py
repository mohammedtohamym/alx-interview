#!/usr/bin/python3
"""Defines island perimeter finding function."""

def island_perimeter(grid):
    """Return the perimeter of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 edges
                perimeter += 4
                # Subtract shared edges with adjacent land
                if i > 0 and grid[i - 1][j] == 1:  # Top neighbor
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Left neighbor
                    perimeter -= 2
    return perimeter
