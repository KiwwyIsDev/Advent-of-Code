def part1(data: list) -> int:
    count = 0
    for line in data:
        print(line)
        cons = line.split(" ")[0]
        con1 = int(cons.split("-")[0])
        con2 = int(cons.split("-")[1])
        char = line.split(" ")[1].split(":")[0]
        strings = line.split(": ")[1]
        print(strings)
        print(con1, con2)
        print(char)
        print(line.count(char))
        if con1 <= strings.count(char) <= con2:
            print(True)
            count += 1
    return count


def part2(data: list) -> int:
    count = 0
    for line in data:
        print(line)
        cons = line.split(" ")[0]
        con1 = int(cons.split("-")[0])
        con2 = int(cons.split("-")[1])
        char = line.split(" ")[1].split(":")[0]
        strings = line.split(": ")[1]
        print(strings)
        print(con1, con2)
        print(char)
        print(strings.count(char))
        if strings[con1 - 1] != strings[con2 - 1] and (
            strings[con1 - 1] == char or strings[con2 - 1] == char
        ):
            print(True)
            count += 1
    return count


with open("data.txt", "r") as file:
    data = [a.strip() for a in file.readlines()]


print(part1(data))
print(part2(data))
