# Determine which games would have been possible if the bag had been loaded with only
# 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

import re

red_goal = 12
green_goal = 13
blue_goal = 14


class Game:
    def __init__(self, ID=None, set1=None, set2=None, set3=None):
        self.ID = ID
        self.set1 = set1
        self.set2 = set2
        self.set3 = set3

    def __str__(self):
        return f"Game ID: {self.ID}, Set1: {self.set1}, Set2: {self.set2}, Set3: {self.set3}"


test_input = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


def pattern_matching(input_string):
    game = Game
    # patter matching:
    # (\d+) : one or more digits
    # ([\w\d\s,]+) : one or more occurrences of word characters, digits, spaces, and commas
    # \s*;\s* : zero or more whitespaces surrounding a semicolon
    pattern = r"Game (\d+): ([\w\d\s,]+)\s*;\s*([\w\d\s,]+)\s*;\s*([\w\d\s,]+)"
    match = re.match(pattern, input_string)

    if match:
        # Extract the groups
        game.ID = match.group(1)
        game.set1 = match.group(2)
        game.set2 = match.group(3)
        game.set3 = match.group(4)
    else:
        print("No match found in: ", input_string)
    return game


def parse_set(set):
    raw_cubes = set.split(",")
    for cube in raw_cubes:
        if " red" in cube:
            cube = cube.replace(" red", "")
            red = int(cube)
        elif " green" in cube:
            cube = cube.replace(" green", "")
            green = int(cube)
        elif " blue" in cube:
            cube = cube.replace(" blue", "")
            blue = int(blue)
        else:
            print("error parsing cube")
    return red, green, blue


def check_set(red, green, blue):
    possible = True
    if (red > 12) and (green > 13) and (blue > 14):
        possible = True
    return possible


file_path = "day1_inputs.txt"

# with open(file_path, "r") as file:
#     input = [line.strip() for line in file]

input = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
test_game = pattern_matching(input)


print(test_game)
