"""
AoC2021 Day 2: Dive!
"""


def part_1():
    """Part 1: 1427868"""
    with open("input.txt", "r", encoding="utf-8") as file_input:
        instructions = file_input.read().split("\n")

    horizontal = 0
    depth = 0

    for instruction in instructions[:-1]:
        direction, num = instruction.split(" ")
        if direction == "up":
            depth -= int(num)
        elif direction == "down":
            depth += int(num)
        else:
            horizontal += int(num)

    print(horizontal * depth)


def part_2():
    """Part 2: 1568138742"""
    with open("input.txt", "r", encoding="utf-8") as file_input:
        instructions = file_input.read().split("\n")

    horizontal = 0
    depth = 0
    aim = 0

    for instruction in instructions[:-1]:
        direction, num = instruction.split(" ")
        if direction == "up":
            aim -= int(num)
        elif direction == "down":
            aim += int(num)
        else:
            horizontal += int(num)
            depth += aim * int(num)

    print(horizontal * depth)


if __name__ == "__main__":
    part_1()
    part_2()
