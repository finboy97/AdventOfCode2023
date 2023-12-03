from source.day_03.day_03 import part_01, part_02

test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_part_01():
    input_list = test_input.split("\n")
    assert part_01(input_list) == 4361

def test_part_02():
    input_list = test_input.split("\n")
    assert part_02(input_list) == 467835
