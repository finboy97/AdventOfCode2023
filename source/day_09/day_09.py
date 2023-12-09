from collections import Counter

input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
# 18 + 28 + 68
# Part 2: 2 + 0 + 5

input = open("source/day_09/input").read()
input = input.splitlines()
input = [x.split() for x in input]

total_new_increments = 0
total_leftside_extrapolations = 0

for sequence in input:
    base_difference_found = False
    input_diff_stack = []
    final_values = []
    leftside_values = []
    input_diff_stack.append(sequence)
    while not base_difference_found:
        current_sequence = input_diff_stack[-1]

        new_diff = []
        for i, value in enumerate(current_sequence):
            if i == 0:
                continue
            new_diff.append(int(value) - int(current_sequence[i-1]))
        if len(Counter(new_diff).most_common()) == 1:
            base_difference_found = True
            final_values.append(new_diff[0])
            leftside_values.append(new_diff[0])
        else:
            input_diff_stack.append(new_diff)

    while len(input_diff_stack) > 0:
        next_level = input_diff_stack.pop()

        next_level.append(int(next_level[-1]) + final_values[-1])
        leftside_values.append(int(next_level[0]) - int(leftside_values[-1]))
        final_values.append(next_level[-1])
    total_new_increments += final_values[-1]
    total_leftside_extrapolations = total_leftside_extrapolations + leftside_values[-1]
    print("\n")

print(total_new_increments)
print(total_leftside_extrapolations)