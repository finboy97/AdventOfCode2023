from collections import defaultdict
import re
import numpy as np

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

z_steps = []
for num in range(0,len(simultaneous_nodes)):
    z_steps.append([])

for i, value in enumerate(simultaneous_nodes):
    current_value = value
    circle_completed = False
    current_instruction = 0
    steps = 0
    first_z = None
    while not circle_completed:
        steps += 1
        if instructions[current_instruction] == "L":
            current_value = location_map[current_value][0]
        else:
            current_value = location_map[current_value][1]
        current_instruction += 1
        if current_value[-1] == "Z":
            if first_z is None:
                first_z = current_value
                z_steps[i].append(steps)
                steps = 0
            elif current_value == first_z:
                z_steps[i].append(steps)
                circle_completed = True
        if current_instruction == len(instructions):
            current_instruction = 0

# Didnt know how to do least common denominator so had to look it up. Found a numpy implementation
z_steps = [max(x) for x in z_steps]
lcm = np.lcm.reduce(z_steps)
print(lcm)