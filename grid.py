def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    string_grid = ""
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            string_grid += grid[i][j].display
            if j == len(grid[i])-1:
                string_grid += "\n "
            j += 1
        i += 1
    return string_grid

#this is wrong as the player is not included and has to take over a space when moved