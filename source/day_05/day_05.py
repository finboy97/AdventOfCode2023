from collections import defaultdict

def part_01(input_list):
    return find_nearest_location(input_list)

def find_nearest_location(input_lst):
    seeds = input_lst[0].split(": ")[-1].split(" ")
    seeds = list(map(lambda x: int(x), seeds))
    list_to_check = input_lst[2:]
    blank_line = False
    seed_edited_this_round = [False for seed in seeds]
    
    for value in list_to_check:
        print(value)
        if len(value)==0:
            blank_line=True
            continue
        if value[0].isdigit() and not blank_line:
            ranges = value.split(" ")
            ranges.append(range(int(ranges[1]), int(ranges[1])+int(ranges[2])))
            for seed in seeds:
                if seed in ranges[3] and not seed_edited_this_round[seeds.index(seed)]:
                    print (f"seed {seed} in {ranges}")
                    diff = int(ranges[0]) - int(ranges[1])
                    print(diff)
                    
                    new_value = int(ranges[0]) + (int(seed) - int(ranges[1]))
                    print(f"New value is {new_value}")
                    seed_index = seeds.index(seed)
                    seeds[seed_index] = new_value
                    seed_edited_this_round[seed_index] = True
        else:
            blank_line = False
            seed_edited_this_round = [False for seed in seeds]
            continue
        
    print(seeds)

    return min(seeds)
            
def part_02():
    return

with open("source/day_05/input") as input_file:
    input_list = input_file.read().split("\n")
    result = part_01(input_list)
    print(result)