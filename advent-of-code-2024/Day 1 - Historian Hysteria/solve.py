from math import prod


with open("data.txt", "r") as file:
    data = [x.split() for x in file.readlines()]
print(data)


def part1():
    a, b, result = [], [], []
    for x in data:
        print(x[0], x[1])
        a.append(int(x[0]))
        b.append(int(x[1]))
    a.sort()
    b.sort()
    for i, v in zip(a, b):
        result.append(abs(i - v))
        print(i, v)
    return sum(result)


def part2():
    a, b, result = [], [], []
    for x in data:
        print(x[0], x[1])
        a.append(int(x[0]))
        b.append(int(x[1]))

    for i in a:
        result.append(i * b.count(i))
    print(result)
    return sum(result)


# print(part1())
print(part2())
