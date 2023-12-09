from collections import defaultdict
import re

test_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

test_input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
test_input = open("input").read()

test_input = test_input.splitlines()
instructions = test_input[0]

location_map = defaultdict()
simultaneous_nodes = []
for value in test_input[2:]:
    current, dest = value.split(" = ")
    dest = (re.findall("[A-Z\d]{3}", dest))
    location_map[current] = dest
    if current[-1] == "A":
        simultaneous_nodes.append(current)

current_instruction = 0
steps = 0
z_reached = False



while not z_reached:
    for i, value in enumerate(simultaneous_nodes):
        if value[-1] != "Z":
            if instructions[current_instruction] == "L":
                simultaneous_nodes[i] = location_map[value][0]
            else:
                simultaneous_nodes[i] = location_map[value][1]

    z_reached = True
    for value in simultaneous_nodes:
        if value[-1] != "Z":
            z_reached = False
    current_instruction += 1
    if current_instruction == len(instructions):
        current_instruction = 0
    steps += 1
    print(simultaneous_nodes)

print(steps)
