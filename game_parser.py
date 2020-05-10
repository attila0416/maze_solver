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
    if counter_x != 1:
        raise ValueError("Expected 1 starting position, got {}.".format(lines.count("X")))

    counter_y = count_character(lines, "Y")
    if counter_y != 1:
        raise ValueError("Expected 1 ending position, got {}.".format(lines.count("Y")))

    possible_teleport_ids = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    check_teleport_pairs(possible_teleport_ids, lines)

    grid = unsafe_parse(possible_teleport_ids, lines)
    return grid


def check_teleport_pairs(possible_teleport_ids, raw_lines):
    occurrences = [0] * len(possible_teleport_ids)
    for raw_line in raw_lines:
        for raw_char in raw_line:
            # Make sure teleports are in pairs
            if raw_char.isdigit():
                int_entry = int(raw_char)
                for occurrence_index in range(0, len(occurrences)):
                    if int_entry == occurrence_index + 1:
                        occurrences[occurrence_index] += 1
                        break
    pad_num = 1
    for occurrence in occurrences:
        if occurrence != 0 and occurrence != 2:
            raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(pad_num))
        pad_num += 1


def unsafe_parse(possible_teleport_ids, raw_lines):
    grid = []
    for raw_line in raw_lines:
        new_line = []

        for raw_char in raw_line:
            if raw_char == "\n":
                pass
            elif raw_char == Start().display:
                new_line.append(Start())
            elif raw_char == End().display:
                new_line.append(End())
            elif raw_char == Air().display:
                new_line.append(Air())
            elif raw_char == Wall().display:
                new_line.append(Wall())
            elif raw_char == Fire().display:
                new_line.append(Fire())
            elif raw_char == Water().display:
                new_line.append(Water())
            elif raw_char in possible_teleport_ids:
                new_line.append(Teleport(int(raw_char)))
            else:
                raise ValueError("Bad letter in configuration file: {}.".format(raw_char))

        grid.append(new_line)
    return grid


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
