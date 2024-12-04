with open("data.txt", "r") as file:
    data = [list(map(int, x.split())) for x in file.readlines()]


print(data)


def is_safe(data: list) -> bool:
    direction = data[1] > data[0]  # True; 1 2
    if direction:
        for i in range(len(data) - 1):

            if not (1 <= data[i + 1] - data[i] <= 3):
                return False

        return True
    else:
        for i in range(len(data) - 1):
            if not (-3 <= data[i + 1] - data[i] <= -1):
                return False
        return True


def part1():
    count = 0
    for x in data:
        count += is_safe(x)

    return count


def part2():
    count = 0
    for x in data:
        if is_safe(x):
            count += 1
        else:
            for i in range(len(x)):
                if is_safe(x[:i] + x[i + 1 :]):
                    count += 1
                    break
    return count


print(part1())
print(part2())
