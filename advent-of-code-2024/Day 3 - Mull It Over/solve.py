from re import finditer

with open("data.txt", "r") as file:
    data = file.read()


def part1():

    s = list(finditer(r"(mul\((\d{1,3}),(\d{1,3})\))", data))
    result = []
    for i in s:

        result.append(int(i.group(2)) * int(i.group(3)))
    return sum(result)


def part2():
    s = list(finditer(r"(mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\))", data))
    result = []
    enabled = True
    for i in s:
        # print(i.group(0))
        # print(i.groups())
        if i.group(1).startswith("mul"):
            if enabled:
                result.append(int(i.group(2)) * int(i.group(3)))

        else:
            enabled = i.group(1) == "do()"
    return sum(result)


print(part1())
print(part2())
