

colour_limits={
    "red": 12,
    "green": 13,
    "blue": 14
}

def part_01(input):
    valid_id_score=0
    for value in input:
        split_input=value.split(":")
        id = split_input[0].split(" ")[-1]
        draw=split_input[-1].replace(";",",")
        
        is_valid=True
        
        for element in draw.split(","):
            value_and_colour = element.strip().split(" ")
            if int(value_and_colour[0]) < 13: # it will always be valid
                continue
            else:
                if int(value_and_colour[0]) > colour_limits[value_and_colour[1]]:
                    is_valid=False
        if is_valid: valid_id_score+=int(id)
    return valid_id_score



def part_02(input):
    total_set_powers = 0
    for value in input:
        min_values={
        "red": 1,
        "blue": 1,
        "green": 1
    }
        split_input=value.split(":")
        draw=split_input[-1].replace(";",",")
        
        for element in draw.split(","):
            value_and_colour = element.strip().split(" ")
            if int(value_and_colour[0]) > min_values[value_and_colour[1]]:
                min_values[value_and_colour[1]] = int(value_and_colour[0])
        set_power=min_values["red"]*min_values["blue"]*min_values["green"]
        total_set_powers+=set_power
    return total_set_powers

with open("source/day_02/day_02_input") as input_file:
    input_str = input_file.readlines()
    print(part_01(input_str))
    print(part_02(input_str))

"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

"""
Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
What is the sum of the IDs of those games?
"""

"""
what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
The power of the minimum set of cubes in game 1 is 48. 
Adding up these five powers produces the sum 2286.
"""