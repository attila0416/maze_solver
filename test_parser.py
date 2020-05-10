from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire, Water, Teleport
)
from game_parser import parse


def test_parse_exactly_1_start_and_end():
    print("Running test_parse_exactly_1_start")
    actual_successful = parse([["X", "Y"]])
    expected_successful = [[Start(), End()]]
    assert actual_successful == expected_successful

    try:
        parse([["Y"]])
        assert False, "Expected exception to be raised"
    except Exception:
        pass

    try:
        parse([["X"]])
        assert False, "Expected exception to be raised"
    except Exception:
        pass


def handle_new_line_chars():
    print("Running handle_new_line_chars")
    input = [["*", "X", "\n"],
             ["*", "Y", "\n"]]
    actual = parse(input)
    expected = [[Wall(), Start()],
                [Wall(), End()]]
    assert actual == expected


def test_parse():
    print("Running test_parse")
    # positive testcase
    input = [["*", "X", "*", "*", "*"],
             ["*", "1", " ", "4", "*"],
             ["*", "4", "1", " ", "*"],
             ["*", "*", "*", "Y", "*"]]
    actual = parse(input)
    expected = [[Wall(), Start(), Wall(), Wall(), Wall()],
                [Wall(), Teleport(1), Air(), Teleport(4), Wall()],
                [Wall(), Teleport(4), Teleport(1), Air(), Wall()],
                [Wall(), Wall(), Wall(), End(), Wall()]]
    # sanity check
    assert Wall() == Wall()
    assert Teleport(1) == Teleport(1)
    assert Air() == Air()
    assert End() == End()
    assert Start() == Start()
    assert Fire() == Fire()
    assert Water() == Water()

    assert actual == expected, "Actual parser output <{}> did not match expected output.".format(grid_str(actual))


def test_read_lines():
    assert True


def run_tests():
    test_parse()
    test_parse_exactly_1_start_and_end()
    handle_new_line_chars()


def grid_str(grid):
    displayable = ""
    for line in grid:
        for cell in line:
            displayable += cell.__repr__()
            displayable += ", "
        displayable += "\n"
    return displayable
