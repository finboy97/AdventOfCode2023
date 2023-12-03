import re

num_regex = re.compile(r"(\d+)")
non_numeric_or_fullstop_regex = re.compile(r"[^\d\.]")

def part_01(list_of_str):
    height = len(list_of_str)
    total_parts_number = 0
    
    for i, line in enumerate(list_of_str):
        length = len(line)
        matches=re.finditer(num_regex, line)
        for run,match in enumerate(matches):
            match_span = match.span()
            start = 0 if match_span[0]< 2 else match_span[0]-1
            end = length-1 if (match_span[1] == length-1) else match_span[1]+1

            present=False
            #Check current line
            if non_numeric_or_fullstop_regex.search(line[start:end]):
                present=True
                
            #check previous line
            if i > 0:
                substr_to_check = list_of_str[i-1][start:end]
                if non_numeric_or_fullstop_regex.search(substr_to_check):
                    present=True
                    
            #check next line
            if i < height-1:
                substr_to_check = list_of_str[i+1][start:end]
                if non_numeric_or_fullstop_regex.search(substr_to_check):
                    present=True

            if present:
                total_parts_number+=int(match.group())
                
    return total_parts_number
                


with open("source/day_03/input") as input_file:
    input_list = input_file.read().split("\n")
    print(part_01(input_list))