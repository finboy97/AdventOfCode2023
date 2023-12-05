from collections import defaultdict

def part_01(input_list):
    seeds = input_list[0].split(": ")[-1].split(" ")
    altered_list = input_list[2:]
    return find_nearest_location(altered_list, seeds)

def find_nearest_location(input_lst, seeds):
    seeds = seeds
    seeds = list(map(lambda x: int(x), seeds))
    list_to_check = input_lst[2:]
    blank_line = False
    seed_edited_this_round = [False for seed in seeds]
    index_to_check=3
    for value in list_to_check:
        if len(value)==0:
            blank_line=True
            continue
        if value[0].isdigit() and not blank_line:
            ranges = value.split(" ")
            ranges.append(range(int(ranges[1]), int(ranges[1])+int(ranges[2])))
            for i, seed in enumerate(seeds):
                print(i)
                if i == index_to_check:
                    print(seed)
                    print(ranges)
                    print(seed in ranges[3])
                    #print(seed_edited_this_round[i])
                if (seed in ranges[3]) and (not seed_edited_this_round[i]):
                    diff = int(ranges[0]) - int(ranges[1])
                    new_value = int(ranges[0]) + (int(seed) - int(ranges[1]))
                    if i == index_to_check:
                        print(f"New value is {new_value}")

                    seed_index = i
                    seeds[seed_index] = new_value
                    seed_edited_this_round[seed_index] = True
        else:
            blank_line = False
            seed_edited_this_round = [False for seed in seeds]
            continue
        
    print(seeds)
    return min(seeds)
            
def part_02(input_list):
    seeds = input_list[0].split(": ")[-1].split(" ")
    seeds = list(map(lambda x: int(x), seeds))
    input_ranges = []
    start = 0
    
    for i, pair in enumerate(seeds):
        if i==0 or i%2==0:
            start = int(pair)
        else:
            seed_range = [*range(start, start+pair)]
            input_ranges = input_ranges + seed_range
            
    altered_list = input_list[2:]
    print(input_ranges)
    return find_nearest_location(altered_list, input_ranges)
    

with open("source/day_05/input") as input_file:
    input_list = input_file.read().split("\n")
    result = part_02(input_list)
    print(result)