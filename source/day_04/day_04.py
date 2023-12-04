

def part_01(list_of_str):
    total_score = 0
    for scratchcard in list_of_str:
        winners,card = scratchcard.split("|")
        total_score+=calc_score(winners,card)
    return total_score
    
def calc_score(winners,card):
    total_winning_nums = 0
    
    winning_nums = winners.split(":")[-1].split(" ")
    for blank in range(winning_nums.count("")):
        winning_nums.remove("")
        
    scratchcard_nums = card.strip().split(" ")
    for blank in range(scratchcard_nums.count("")):
        scratchcard_nums.remove("")
    
    for value in scratchcard_nums:
        if value in winning_nums:
            total_winning_nums+=1
    if total_winning_nums>0:
        return 2**(total_winning_nums-1)
    else: return 0



# 28798 too high
# Correct: 27454

def part_02():
    pass

with open("source/day_04/input") as input_file:
    input_list = input_file.read().split("\n")
    print(part_01(input_list))