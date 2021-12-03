"""
AoC2021 Day 3: Binary Diagnostic
"""


def most_common_bit(nums: list, col: int, default: int) -> int:
    """Returns the most common bit in the given column of the provided nums."""
    zeroes = 0
    ones = 0
    for num in nums:
        if num[col] == "0":
            zeroes += 1
        else:
            ones += 1

    if zeroes > ones:
        return 0
    if ones > zeroes:
        return 1
    return default


def inverse(num: str) -> str:
    """Returns the provided string with 0s and 1s swapped."""
    output = ""
    for char in num:
        if char == "0":
            output += "1"
        else:
            output += "0"

    return output


def part_1():
    """Part 1: 3148794"""
    with open("input.txt", "r", encoding="utf-8") as file_input:
        nums = file_input.read().split("\n")[:-1]

    ones = str(nums[0])
    zeroes = inverse(ones)
    ones = [int(one) for one in ones]
    zeroes = [int(zero) for zero in zeroes]

    num_length = len(nums[0])

    gamma = ""
    for i in range(0, num_length):
        gamma += str(most_common_bit(nums, i, 0))
    epsilon = inverse(gamma)

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print(gamma * epsilon)


def part_2():
    """Part 2: 2795310"""
    with open("input.txt", "r", encoding="utf-8") as file_input:
        nums = file_input.read().split("\n")[:-1]

    num_length = len(nums[0])

    oxygen_nums = nums.copy()
    for i in range(0, num_length):
        if len(oxygen_nums) == 1:
            break

        most_common = most_common_bit(oxygen_nums, i, 1)
        oxygen_nums = [num for num in oxygen_nums if int(num[i]) == most_common]

    oxygen_rating = int(oxygen_nums[0], 2)

    carbon_nums = nums.copy()
    for i in range(0, num_length):
        if len(carbon_nums) == 1:
            break

        most_common = most_common_bit(carbon_nums, i, 1)
        carbon_nums = [num for num in carbon_nums if int(num[i]) != most_common]

    carbon_rating = int(carbon_nums[0], 2)

    print(oxygen_rating * carbon_rating)


if __name__ == "__main__":
    part_1()
    part_2()
