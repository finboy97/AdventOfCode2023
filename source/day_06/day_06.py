

def check_time_beats_record(time_held, limit, record):
    """time held also equals distance/milisec"""
    moving_time = limit-time_held
    distance_covered = moving_time * time_held
    return distance_covered > record


with open("source/day_06/input") as input:
    input = input.read().split("\n")



times = input[0].split(":")[1].strip().split()

records = input[1].split(":")[1].strip().split()

winning_times = []
for i, value in enumerate(times):
    record = int(records[i])
    lower_established = False
    lower, upper = 0, 0
    for num in range(0, int(value)):
        result = check_time_beats_record(num, int(value), record)
        if not result and not lower_established:
            continue
        elif result and not lower_established:
            lower = num
            upper = num
            lower_established = True
        elif result and lower_established:
            upper = num
            
        elif not result and lower_established:
            winning_times.append(upper-lower+1)
            break

multiplied_winners = 1
for value in winning_times:
    multiplied_winners *= value
print(multiplied_winners)

#Part 2 - one big race, rather than individual races
# Smarter way to do it - perpendicular bisector to find min and max
# Tired way to do it - bruteforce


big_time = ""
for value in times:
    big_time = big_time + value
big_time = int(big_time)
big_record = ""
for value in records:
    big_record = big_record + value
big_record = int(big_record)

lower_established = False
lower, upper = 0, 0
for num in range(0, big_time):
    result = check_time_beats_record(num, big_time, big_record)
    if not result and not lower_established:
        continue
    elif result and not lower_established:
        lower = num
        upper = num
        lower_established = True
    elif result and lower_established:
        upper = num
        
    elif not result and lower_established:
        upper = num
        break
    
print(upper-lower)
