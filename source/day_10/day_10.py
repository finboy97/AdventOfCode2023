
input = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""


input = open("/Users/finbar/PycharmProjects/AdventOfCode2023/source/day_10/input").read()
input = input.splitlines()
two_d_map = []
start_position = 0
dots = set()
for i, value in enumerate(input):
    new_row = []
    for j, alphanum in enumerate(value):

        new_row.append((i, j, alphanum))
        if alphanum == "S":
            start_position = (i, j, alphanum)
        if alphanum == ".":
            dots.add((i, j, alphanum))
    two_d_map.append(new_row)

height = len(two_d_map)
length = len(two_d_map[0])

edge_dots = set()
for dot in dots:
    if dot[0] == 0 or dot[0] == height -1:
        edge_dots.add(dot)
    elif dot[1] == 0 or dot[1] == length -1:
        edge_dots.add(dot)

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

#Idea - pick dots on the edge. Traverse every neighbour until exhausted. Subtract from total dots at the end.

#Cant do part 2. Not even close. Need to come back to do it. Answer should be 601
#===========================================================
for row in two_d_map:
    current_str = ""
    for element in row:
        if element in start_loop:
            current_str = current_str + element[2]
        elif element in edge_dots:
            current_str = current_str + "o"
        else:
            current_str = current_str + "."



# Structure to track visited dots
visited_dots = set()
positions_to_visit = edge_dots

def get_neighbours(position):
    row, col = position[0], position[1]

    if col > 0:
        left = two_d_map[row][col -1]
        if left not in visited_dots and left[2] == "." and left not in positions_to_visit:
            positions_to_visit.add(left)
    if col < length -1:
        right = two_d_map[row][col + 1]
        if right not in visited_dots and right[2] == "." and right not in positions_to_visit:
            positions_to_visit.add(right)
    if row > 0:
        up = two_d_map[row - 1][col]
        if up not in visited_dots and up[2] == "." and up not in positions_to_visit:
            positions_to_visit.add(up)
    if row < height -1:
        down = two_d_map[row + 1][col]
        if down not in visited_dots and down[2] == "." and down not in positions_to_visit:
            positions_to_visit.add(down)


#while len(positions_to_visit) > 0:
#    current_position = positions_to_visit.pop()
#    get_neighbours(current_position)
#    visited_dots.add(current_position)

dots_not_edges = dots - edge_dots
print(len(dots))
print(len(visited_dots))

str_map = []
for row in two_d_map:
    line_str = ""
    for value in row:
        line_str = line_str +value[2] if value in start_loop else line_str + "."
    line_str = line_str.replace("L7", "--")
    line_str = line_str.replace("FJ", "--")
    str_map.append(line_str)


current_outside_dots = len(edge_dots)

for value in dots_not_edges:
    row = str_map[value[0]]
    x = value[1]
    lj_buffer = []
    counter = 0
    while x > 0:
        x -= 1
        if row[x] == "|":
            counter += 1
            if len(lj_buffer) > 0:
                counter+=1
                lj_buffer = []
        elif row[x] in "-.":
            continue
        elif row[x] in "JL":
            if len(lj_buffer) > 0:
                if "F7" in lj_buffer[0]:
                    counter += 1
                    lj_buffer = []
                elif "JL" in lj_buffer[0]:
                    lj_buffer = []
                    continue
                else:
                    lj_buffer.append(row[x])
            else:
                lj_buffer.append(row[x])
        elif row[x] in "F7":
            if len(lj_buffer) > 0:
                if "JL" in lj_buffer[0]:
                    counter += 1
                    lj_buffer = []
                elif "F7" in lj_buffer[0]:
                    lj_buffer = []
                    continue
                else:
                    lj_buffer.append(row[x])
    if counter % 2 != 0 or counter == 0:
        current_outside_dots += 1

print(len(dots) - current_outside_dots)