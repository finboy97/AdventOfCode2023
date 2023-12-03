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
                
asterisk = re.compile("(\*)")

def part_02(list_of_str):
    height = len(list_of_str)
    total_gear_ratio = 0
    
    for i, line in enumerate(list_of_str):
        length = len(line)
        matches=re.finditer(asterisk, line)
        for run,match in enumerate(matches):
            match_span = match.span()
            start = 0 if match_span[0]< 2 else match_span[0]-1
            end = length-1 if (match_span[1] == length) else match_span[1]
            numbers_to_add = []
            
            #Check current line
            numbers_on_line=re.finditer(num_regex, line)
            if numbers_on_line != None:
                for number in numbers_on_line:
                    number_range = range(number.span()[0], number.span()[1])
                    num_adjacent=False
                    if (start in number_range) or (end in number_range):
                        num_adjacent=True
                    if num_adjacent:
                        numbers_to_add.append(number.group())
                        
            #check previous line
            if i > 0:
                numbers_above = re.finditer(num_regex, list_of_str[i-1])
                for number in numbers_above:
                    number_range = range(number.span()[0], number.span()[1])
                    num_adjacent=False
                    for value in range(start, end+1):
                        if value in number_range:
                            num_adjacent=True
                    if num_adjacent:
                        numbers_to_add.append(number.group())
                    
            #check next line
            if i < height-1:
                numbers_below = re.finditer(num_regex, list_of_str[i+1])
                for number in numbers_below:
                    number_range = range(number.span()[0], number.span()[1])
                    num_adjacent=False
                    print(f"{start}, {end}, {number_range}")
                    for value in range(start, end+1):
                        if value in number_range:
                            num_adjacent=True
                    if num_adjacent:
                        numbers_to_add.append(number.group())

            print(numbers_to_add)
            if len(numbers_to_add)==2:
                total_gear_ratio+=(int(numbers_to_add[0])*int(numbers_to_add[1]))
                
    return total_gear_ratio
                
    

with open("source/day_03/input") as input_file:
    input_list = input_file.read().split("\n")
    print(part_01(input_list))
    print(part_02(input_list))