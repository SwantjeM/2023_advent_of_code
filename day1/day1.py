## Advent of Code 2023
## Day 1
## SwantjeM


## Part 1

file_path = "day1_inputs.txt"

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

word_to_number = {
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


coordinates = []

for line in input:
    coord = []
    # find all occurences of numbers (in "values"), including those sharing letters or occurring multiple times.
    for value in values:
        index = -1
        while True:
            index = line.find(value, index + 1)
            if index == -1:
                break
            coord.append((value, index))

    # sort all numbers in order of occurence
    coord.sort(key=lambda x: x[1])
    clean_coord = [word[0] for word in coord]

    # replace all words with corresponding numbers
    numbers = [str(word_to_number.get(word, word)) for word in clean_coord]

    clean_numbers = numbers[0] + numbers[-1]
    coordinates.append(clean_numbers)


sum = 0
for coordinate in coordinates:
    sum = sum + int(coordinate)


print("Part 2: The final value is: ", sum)
