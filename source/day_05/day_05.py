from collections import defaultdict

def part_01(input_list):
    seeds = input_list[0].split(": ")[-1].split(" ")
    altered_list = input_list[2:]
    return find_nearest_location(altered_list, seeds)

def find_nearest_location(input_lst, seeds):
    seed_ranges = seeds

    list_to_check = input_lst[2:]
    blank_line = False
    seed_edited_this_round = [False for seed in seeds]

    for line in list_to_check:
        if len(line)==0: # empty line signals end of one map
            blank_line=True
            continue
        
        elif line[0].isdigit() and not blank_line: # 
            ranges = line.split(" ")
            source_start = int(ranges[1])
            source_end = int(ranges[2]) + int(ranges[1]) -1
            
            counter = 0
            while counter < len(seeds):
                print(len(seeds))
                print(seed_edited_this_round)
                if seed_edited_this_round[counter]:
                    counter+=1
                    continue
                else:
                    seed = seeds[counter]
                    is_overlap = check_seeds_in_range(source_start, source_end, seed)
                    print(is_overlap)
                    match is_overlap:
                        case "END":
                            print(f"Seed: {seed}, start: {source_start}, breakpoint: {source_end}")
                            to_add, to_change = split_overlap_into_new_ranges(seed, is_overlap, source_start)
                            diff = int(ranges[0]) - int(ranges[1])
                            to_change = [to_change[0]+diff, to_change[1]+diff]
                            seeds[counter] = to_change
                            seed_edited_this_round[counter] = True
                            seeds.append(to_add)
                            seed_edited_this_round.append(False)
                            counter+=1     
                            continue
                        case "INSIDE":
                            diff = int(ranges[0]) - int(ranges[1]) # Difference between source and dest
                            print(ranges)
                            print(f"seed {seed}, diff {diff}")
                            print(f"seed {seed}, range {source_start}, {source_end}")      
                            seed=[seed[0]+diff, seed[1]+diff]                     
                            print(seed)
                            seeds[counter] = seed
                            seed_edited_this_round[counter] = True
                            counter+=1     
                            continue
                        case "OUTSIDE":
                            print(f"seed {seed}, range {source_start}, {source_end}")

                            counter+=1     
                            continue
                        case "START":
                            print(f"Seed: {seed}, start: {source_start}, breakpoint: {source_end}")
                            to_change, to_add = split_overlap_into_new_ranges(seed, is_overlap, source_end)
                            diff = int(ranges[0]) - int(ranges[1])
                            to_change = [to_change[0]+diff, to_change[1]+diff]
                            seeds[counter] = to_change
                            seed_edited_this_round[counter] = True
                            seeds.append(to_add)
                            seed_edited_this_round.append(False)
                            counter+=1     
                            continue
                        case "OVERLAP":
                            print(f"Seed: {seed}, start: {source_start}, breakpoints: {ranges}")
                            unaltered_slice_start, sliced_to_change, unaltered_slice_end = split_overlap_into_new_ranges(seed, is_overlap, [int(ranges[1]), int(ranges[1])+int(ranges[2])])
                            #list 1 - normal up to included
                            seeds.append(unaltered_slice_start)
                            seed_edited_this_round.append(False)
                            # list 3 - included+1 to end
                            seeds.append(unaltered_slice_end)
                            seed_edited_this_round.append(False)
                            # list 2 - slice
                            diff = int(ranges[0]) - int(ranges[1])
                            sliced_to_change = [sliced_to_change[0]+diff, sliced_to_change[1]+diff]
                            seeds[counter] = sliced_to_change
                            seed_edited_this_round[counter] = True
                            counter+=1 
                        case "OTHER":
                            counter+=1 
                            return ValueError(f"Range checking failed for {seed} in range {source_start}, {source_end}")
                    
        else:
            seed_edited_this_round = [False for seed in seeds]
            blank_line=False

                    
                
    return min(min(seeds))
            

def check_seeds_in_range(start,end,seeds):
    #Check wholly inside:
    if seeds[0] > end or seeds[1] < start:
        return "OUTSIDE"
    #Check wholly outside:
    elif seeds[0] >= start and seeds[1] <= end:
        return "INSIDE"
    #Check start of seeds inside the range
    elif start <= seeds[0] <= end:
        return "START"
    #Else end of seeds inside the range
    elif start <= seeds[1] <= end:
        return "END"
    elif seeds[0] < start and end < seeds[1]:
        return "OVERLAP"
    else:
        return "OTHER"

def split_overlap_into_new_ranges(seed, type, end_to_break_on):
    match type:
        case "START": # If the start of the seed range overlaps the start of the range check
            start_num = end_to_break_on
            start_part=[seed[0], start_num] # Make one new seed range for existing start up to and including the end of the range check
            end_part = [start_num+1, seed[1]] # Make a second new seed range for range+1 to end of range check
            return start_part, end_part
        case "END": 
            end_num = end_to_break_on
            start_part=[seed[0], end_num-1]
            end_part = [end_num, seed[1]]
            return start_part, end_part
        case "OVERLAP": 
            print(f"Break: {end_to_break_on}, seed: {seed}")
            start= end_to_break_on[0]
            end = end_to_break_on[1]
            unaltered_slice_start = [seed[0], start-1]
            sliced_to_change = [start, end]
            unaltered_slice_end = [end+1, seed[1]]
            return unaltered_slice_start, sliced_to_change, unaltered_slice_end

def part_02(input_list):
    seeds = input_list[0].split(": ")[-1].split(" ")
    seeds = list(map(lambda x: int(x), seeds))
    input_ranges = []
    start = 0
    end=0
    for i, pair in enumerate(seeds):
        if i==0 or i%2==0:
            start = int(pair)
        else:
            end = start + int(pair)-1
            input_ranges.append([start, end])

    return find_nearest_location(input_list, input_ranges)
    

with open("source/day_05/input") as input_file:
    input_list = input_file.read().split("\n")
    result = part_02(input_list)
    print(result)

# Answer was 125742456
# Spent ages with answer 125742457, until I realised I was not subtracting 1 from the range of seeds 
# (see line 152 for what it should be. Previously it didn't have the minus 1)