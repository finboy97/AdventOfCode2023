from pathlib import Path

input = open("/Users/finbar/PycharmProjects/AdventOfCode2023/source/day_10/input").read()
input = input.splitlines()
two_d_map = []
start_position = 0
for i, value in enumerate(input):
    new_row = []
    for j, alphanum in enumerate(value):
        new_row.append((i, j, alphanum))
        if alphanum == "S":
            start_position = (i, j, alphanum)
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