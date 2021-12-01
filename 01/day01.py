"""
AoC2021 Day 1: Sonar Sweep
"""


def part_1():
    """Part 1: 1451"""
    with open("input.txt", "r", encoding="utf-8") as file_input:
        depths = file_input.read().split("\n")

    depths = [int(depth) for depth in depths[:-1]]

    increases = 0
    previous = depths[0]
    for depth in depths[1:]:
        if depth > previous:
            increases += 1
        previous = depth

    print(increases)


def part_2():
    """Part 2: 1395"""
    with open("input.txt", "r", encoding="utf-8") as file_input:
        depths = file_input.read().split("\n")

    depths = [int(depth) for depth in depths[:-1]]

    increases = 0
    previous = depths[0]
    for i, _ in enumerate(depths[1:-2]):
        if sum(depths[i : i + 3]) > previous:
            increases += 1
        previous = sum(depths[i : i + 3])

    print(increases)


if __name__ == "__main__":
    part_1()
    part_2()
