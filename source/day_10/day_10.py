
input = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""

#input = open("/Users/finbar/PycharmProjects/AdventOfCode2023/source/day_10/input").read()
input = input.splitlines()
two_d_map = []
start_position = 0
dots = []
for i, value in enumerate(input):
    new_row = []
    for j, alphanum in enumerate(value):
        new_row.append((i, j, alphanum))
        if alphanum == "S":
            start_position = (i, j, alphanum)
        if alphanum == ".":
            dots.append((i, j, alphanum))
    two_d_map.append(new_row)

height = len(two_d_map)
length = len(two_d_map[0])

for row in two_d_map:
    print(row)
visited_locations = set()
start_loop = []


def get_location_from_start(start):
    row, col = start[0], start[1]

    if (col - 1) >= 0:
        left = two_d_map[row][col - 1]
        if left[2] in "L-F":
            return left
    if (row - 1) >= 0:
        above = two_d_map[row - 1][col]
        if above[2] in "F7|":
            return above
    if (col + 1) < length:
        right = two_d_map[row][col + 1]
        if right[2] in "7J-":
            return right
    else:
        return two_d_map[row + 1][col]


def is_loop_closed(pos_1, pos_2):
    return pos_1 in visited_locations and pos_2 in visited_locations


def get_next_location(position):

    row, col = position[0], position[1]

    if position[2] == "L":
        above = two_d_map[row - 1][col]
        right = two_d_map[row][col + 1]
        if is_loop_closed(above, right): return None
        return above if right  in visited_locations else right
    elif position[2] == "-":
        left = two_d_map[row][col - 1]
        right = two_d_map[row][col + 1]
        if is_loop_closed(left, right): return None
        return left if right in visited_locations else right
    elif position[2] == "|":
        above = two_d_map[row - 1][col]
        below = two_d_map[row + 1][col]
        if is_loop_closed(above, below): return None
        return above if below in visited_locations else below
    elif position[2] == "7":
        left = two_d_map[row][col - 1]
        below = two_d_map[row + 1][col]
        if is_loop_closed(left, below): return None
        return left if below in visited_locations else below
    elif position[2] == "F":
        right = two_d_map[row][col + 1]
        below = two_d_map[row + 1][col]
        if is_loop_closed(below, right): return None
        return right if below in visited_locations else below
    elif position[2] == "J":
        left = two_d_map[row][col - 1]
        above = two_d_map[row + -1][col]
        if is_loop_closed(above, left): return None
        return left if above in visited_locations else above
    else:
        return None


next_location = get_location_from_start(start_position)
start_loop.append(start_position)
visited_locations.add(start_position)
steps = 0
while next_location is not None:
    current = next_location
    visited_locations.add(current)
    next_location = get_next_location(current)
    start_loop.append(current)


print(int(len(start_loop) / 2))

# No idea. Hint said to count how many times it crosses over the loop.

for row in two_d_map:
    current_str = ""
    for element in row:
        current_str = current_str + element[2] if element in start_loop else current_str + "."
    print(current_str)

map_of_just_loop = []
for row in two_d_map:
    updated_row = []
    for position in row:
        if position in start_loop:
            updated_row.append(position)
        else:
            new_pos = (position[0], position[1], ".")
            updated_row.append(new_pos)
    map_of_just_loop.append(updated_row)




def is_position_in_loop(position):
    row, col = position[0], position[1]
    x = col -1
    crosses = 0
    while x >= 0:
        pos_to_check = map_of_just_loop[row][x]
        if pos_to_check in start_loop:
            left_blocks = "|"
            up_path = "LJ"
            down_path = "F7"
            if pos_to_check[2] in left_blocks:
                crosses += 1
            elif pos_to_check[2] in left_blocks:
                if last_cross
        x -= 1
    if crosses % 2 == 0 or crosses == 0:
        return 0

    y = row -1
    crosses = 0
    while y >= 0:
        pos_to_check = map_of_just_loop[y][col]
        if pos_to_check in start_loop:
            up_blockers = "-JLF7"
            if pos_to_check[2] in up_blockers:
                crosses += 1
        y -= 1
    if crosses % 2 == 0 or crosses == 0:
        return 0
    return 1

total_inside_loop = 0
for value in dots:
    total_inside_loop += is_position_in_loop(value)

print(total_inside_loop)
#print(is_position_in_loop((6, 2)))

"""
[(0, 0, '.'), (0, 1, '.'), (0, 2, '.'), (0, 3, '.'), (0, 4, '.'), (0, 5, '.'), (0, 6, '.'), (0, 7, '.'), (0, 8, '.'), (0, 9, '.')]
[(1, 0, '.'), (1, 1, 'S'), (1, 2, '-'), (1, 3, '-'), (1, 4, '-'), (1, 5, '-'), (1, 6, '-'), (1, 7, '-'), (1, 8, '7'), (1, 9, '.')]
[(2, 0, '.'), (2, 1, '|'), (2, 2, 'F'), (2, 3, '-'), (2, 4, '-'), (2, 5, '-'), (2, 6, '-'), (2, 7, '7'), (2, 8, '|'), (2, 9, '.')]
[(3, 0, '.'), (3, 1, '|'), (3, 2, '|'), (3, 3, '.'), (3, 4, '.'), (3, 5, '.'), (3, 6, '.'), (3, 7, '|'), (3, 8, '|'), (3, 9, '.')]
[(4, 0, '.'), (4, 1, '|'), (4, 2, '|'), (4, 3, '.'), (4, 4, '.'), (4, 5, '.'), (4, 6, '.'), (4, 7, '|'), (4, 8, '|'), (4, 9, '.')]
[(5, 0, '.'), (5, 1, '|'), (5, 2, 'L'), (5, 3, '-'), (5, 4, '7'), (5, 5, 'F'), (5, 6, '-'), (5, 7, 'J'), (5, 8, '|'), (5, 9, '.')]
[(6, 0, '.'), (6, 1, '|'), (6, 2, '.'), (6, 3, '.'), (6, 4, '|'), (6, 5, '|'), (6, 6, '.'), (6, 7, '.'), (6, 8, '|'), (6, 9, '.')]
[(7, 0, '.'), (7, 1, 'L'), (7, 2, '-'), (7, 3, '-'), (7, 4, 'J'), (7, 5, 'L'), (7, 6, '-'), (7, 7, '-'), (7, 8, 'J'), (7, 9, '.')]
[(8, 0, '.'), (8, 1, '.'), (8, 2, '.'), (8, 3, '.'), (8, 4, '.'), (8, 5, '.'), (8, 6, '.'), (8, 7, '.'), (8, 8, '.'), (8, 9, '.')]
"""