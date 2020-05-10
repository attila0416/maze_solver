from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""
    try:
        txt_file = open(filename, "r")
    except FileNotFoundError:
        print("{} does not exist!".format(filename))
        exit()
    except OSError:
        print("File not open for reading")
        exit()

    lines = []
    while True:
        line = txt_file.readline()
        if line == "":
            break
        split_list = list(line)
        lines.append(split_list)
    grid = parse(lines)
    return grid


def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
    counter_x = count_character(lines, "X")
    counter_y = count_character(lines, "Y")

    occurrences = [0] * 9
    list_of_cells = [[]] * len(lines)
    i = 0
    while i < len(lines):
        for entry in lines[i]:
            if entry.isdigit():
                int_entry = int(entry)
                for occurrence_index in range(0, len(occurrences)):
                    if int_entry == occurrence_index + 1:
                        occurrences[occurrence_index] += 1
                        break
        j = 0
        while j < len(lines[i]):
            if lines[i][j] == "\n":
                lines[i].pop(j)
            if lines[i][j] == Start().display:
                list_of_cells[i][j] = Start()
            elif lines[i][j] == End().display:
                list_of_cells[i][j] = End()
            elif lines[i][j] == Air().display:
                list_of_cells[i][j] = Air()
            elif lines[i][j] == Wall().display:
                list_of_cells[i][j] = Wall()
            elif lines[i][j] == Fire().display:
                list_of_cells[i][j] = Fire()
            elif lines[i][j] == Water().display:
                list_of_cells[i][j] = Water()
            elif lines[i][j] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                list_of_cells[i][j] = Teleport(int(lines[i][j]))

            if lines[i][j] != "X" and \
                    lines[i][j] != "Y" and \
                    lines[i][j] != "F" and \
                    lines[i][j] != "W":
                raise ValueError("Bad letter in configuration file: {}.".format(lines[i][j]))
            if counter_x != 1:
                raise ValueError("Expected 1 starting position, got {}.".format(lines.count("X")))
            if counter_y != 1:
                raise ValueError("Expected 1 starting position, got {}.".format(lines.count("Y")))
            j += 1
        i += 1
    pad_num = 1
    for occurrence in occurrences:
        if occurrence != 0 and occurrence != 2:
            raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(pad_num))
        pad_num += 1
    return list_of_cells


def count_character(lines, character):
    i = 0
    counter = 0
    while i < len(lines):
        j = 0
        while j < len(lines[i]):
            if lines[i][j] == character:
                counter += 1
            j += 1
        i += 1
    return counter

# grid = read_lines("board_hard.txt")
# print(grid)
