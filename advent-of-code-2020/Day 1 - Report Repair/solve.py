def part1(data: list) -> int:
    for i in data:
        for j in data:
            if i + j == 2020:
                return i * j


def part2(data: list) -> int:
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    return i * j * k


with open("data.txt", "r") as file:
    data = [int(a) for a in file.readlines()]
    print(part1(data))
    print(part2(data))
