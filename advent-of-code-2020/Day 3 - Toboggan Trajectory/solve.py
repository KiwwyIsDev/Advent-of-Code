from math import prod

with open("data.txt", "r") as file:
    data = [a.strip() for a in file.readlines()]


def solve(right_step: int, bottom: int, text=data):
    x = y = count = 0
    for y in range(0, len(text), bottom):

        if data[y][x] == "#":
            count += 1

        x += right_step
        x = x % len(data[0])

    return count


# print(data)
print(solve(3, 1))
print(prod((solve(1, 1), solve(3, 1), solve(5, 1), solve(7, 1), solve(1, 2))))
