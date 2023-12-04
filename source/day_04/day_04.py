from collections import defaultdict

card_tracker = defaultdict(int)

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

def part_02(list_of_str):
    for scratchcard in list_of_str:
        process_card(scratchcard)
        print(card_tracker.values())
    total_tickets = 0
    for value in card_tracker.values():
        total_tickets+=value
    return total_tickets
            
        
        

def process_card(scratchcard):
    winners, card = scratchcard.split("|")
    winning_nums = winners.split(":")[-1].split(" ")
    card_id = winners.split(":")[0].split(" ")[-1]
    
    card_tracker[card_id]+=1 #Plus 1 for being called
    for blank in range(winning_nums.count("")):
        winning_nums.remove("")

    scratchcard_nums = card.strip().split(" ")
    for blank in range(scratchcard_nums.count("")):
        scratchcard_nums.remove("")
    
    total_winners = 0
    for value in scratchcard_nums:
        if value in winning_nums:
            total_winners+=1
    print(f"Card: {card_id} has {total_winners} winners and {card_tracker[card_id]} appearances")

    for winning_ticket in range(int(card_id)+1, int(card_id)+1+total_winners): #Add another set of winners
        card_tracker[f"{winning_ticket}"] += 1*card_tracker[card_id]

with open("source/day_04/input") as input_file:
    input_list = input_file.read().split("\n")
    print(part_01(input_list))
    print(part_02(input_list))