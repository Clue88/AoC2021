"""
AoC2021 Day 4: Giant Squid
"""


def check_num(num, board):
    """Replaces instances of the given number with an X."""
    for row in board:
        for i, item in enumerate(row):
            if item == num:
                row[i] = "X"


def check_winner(board):
    """Returns True if the board is a winning board."""
    for row in board:
        is_winner = True
        for item in row:
            if item != "X":
                is_winner = False
                break
        if is_winner:
            return True

    for col in range(0, len(board[0])):
        is_winner = True
        for row in board:
            if row[col] != "X":
                is_winner = False
                break
        if is_winner:
            return True

    return False


def part_1():
    """Part 1: 35670"""
    with open("input.txt", "r", encoding="utf-8") as file_input:
        sections = file_input.read().strip().split("\n\n")

    nums = sections[0].split(",")
    boards = []
    for section in sections[1:]:
        curr_board = []
        for line in section.split("\n"):
            curr_board.append(line.split())
        boards.append(curr_board)

    winning_num = 0
    winning_board = []
    for num in nums:
        found_winner = False
        for board in boards:
            check_num(num, board)
            if check_winner(board):
                winning_board = board
                found_winner = True
                break
        if found_winner:
            winning_num = num
            break

    total = 0
    for row in winning_board:
        for item in row:
            if item != "X":
                total += int(item)

    print(total * int(winning_num))


def part_2():
    """Part 2: 22704"""
    with open("input.txt", "r", encoding="utf-8") as file_input:
        sections = file_input.read().strip().split("\n\n")

    nums = sections[0].split(",")
    boards = []
    for section in sections[1:]:
        curr_board = []
        for line in section.split("\n"):
            curr_board.append(line.split())
        boards.append(curr_board)

    last_num = 0
    last_board = []
    winners = []
    for num in nums:
        last_num = num
        for board in boards:
            if board in winners:
                continue
            check_num(num, board)
            if check_winner(board):
                winners.append(board)
                last_board = board
        if len(winners) == len(boards):
            break

    total = 0
    for row in last_board:
        for item in row:
            if item != "X":
                total += int(item)

    print(total * int(last_num))


if __name__ == "__main__":
    part_1()
    part_2()
