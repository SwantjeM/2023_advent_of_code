## Advent of Code 2023
## Day 1
## Puzzle 1
## Swantje Moehle


## Part 1
file_path = "day1_1_inputs.txt"
with open(file_path, "r") as file:
    input = [line.strip() for line in file]

coordinates = []

for line in input:
    numbers = "".join(char for char in line if char.isdigit())
    clean_numbers = numbers[0] + numbers[-1]
    coordinates.append(clean_numbers)

sum = 0
for coordinate in coordinates:
    sum = sum + int(coordinate)

print("Part 1: The final value is: ", sum)

## Part 2
values = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

word_to_number: {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

new_coordinates = []

for line in input:
    coord = []
    for value in values:
        if value in line:
            coord.append(value)
            # print(coord)
    new_coordinates.append(coord)


for line in input:
    coord = []
    for value in values:
        index = line.find(value)
        if index != -1:
            coord.append((value, index))
    sorted_coord = sorted(coord, key=lambda x: x[1])
    cleaned_coord = [word[0] for word in sorted_coord]
    print(cleaned_coord)


# print(new_coordinates)
