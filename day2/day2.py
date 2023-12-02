# Determine which games would have been possible if the bag had been loaded with only
# 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?


class Game:
    def __init__(self, ID=None, set1=None, set2=None, set3=None):
        self.ID = ID
        self.sets = []


test_input = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


def pattern_matching(input_string):
    game = Game
    first_split = input_string.split(":")
    print(first_split[0])
    print(first_split[1])

    if "Game " in first_split[0]:
        game.ID = first_split[0].replace("Game ", "")
        print(game.ID)
    else:
        print("Error, no Game in ", first_split[0])

    game.sets = first_split[1].split(";")
    print(game.sets)

    return game


def parse_set(set):
    print(set)
    raw_cubes = set.split(",")
    red = 0
    green = 0
    blue = 0
    for cube in raw_cubes:
        print(cube)
        if " red" in cube:
            cube = cube.replace(" red", "")
            red = int(cube)
        elif " green" in cube:
            cube = cube.replace(" green", "")
            green = int(cube)
        elif " blue" in cube:
            cube = cube.replace(" blue", "")
            blue = int(cube)
            print("BLUE!", blue)
        else:
            print("error parsing cube")
        print(cube)
        print("r g b", red, green, blue)
    return [red, green, blue]


def check_set(colors):
    red = colors[0]
    green = colors[1]
    blue = colors[2]
    possible = False
    if (red <= 12) and (green <= 13) and (blue <= 14):
        possible = True
    return possible


file_path = "day2_inputs.txt"

with open(file_path, "r") as file:
    input = [line.strip() for line in file]

# input = [
#     "Game 82: 2 green, 7 blue, 2 red; 15 blue, 2 green, 1 red; 3 blue, 2 green; 1 red; 2 red, 15 blue, 2 green"
# ]

poss = []
result = 0
for line in input:
    # input = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    test_game = pattern_matching(line)
    possible = []
    for set in test_game.sets:
        possible.append(check_set(parse_set(set)))
    # print(possible)

    if all(possible):
        print(possible)
        print("Game: ", test_game.ID, " is possible")
        result = result + int(test_game.ID)
        print(int(test_game.ID))
        print(result)
        poss.append(int(test_game.ID))

    else:
        # print("Game: ", test_game.ID, " is impossible")
        pass

print(result)
print(poss)
print(sum(poss))


# print(test_game)
