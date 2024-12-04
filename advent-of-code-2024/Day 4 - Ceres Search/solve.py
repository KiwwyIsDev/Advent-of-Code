with open("data.txt", "r") as file:
    data = [list(x.strip()) for x in file.readlines()]


def part1():
    d = []

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == dy == 0:
                continue
            d.append((dx, dy))

    def is_xmas(i, j, d):
        dx, dy = d
        word = "XMAS"
        for k in range(len(word)):
            i2 = i + k * dx
            j2 = j + k * dy
            if not (0 <= i2 < len(data) and 0 <= j2 < len(data[0])):
                return False
            if data[i2][j2] != word[k]:
                return False

        return True

    count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            for _d in d:
                count += is_xmas(i, j, _d)

    return count


def part2():
    def is_xmas(i, j):
        if not (1 <= i < len(data) - 1 and 1 <= j < len(data[0]) - 1):
            return False
        if data[i][j] != "A":
            return False

        diagonal_l2r = f"{data[i - 1][j - 1]}{data[i + 1][j + 1]}"
        diagonal_r2l = f"{data[i - 1][j + 1]}{data[i + 1][j - 1]}"
        here = ["SM", "MS"]
        return diagonal_l2r in here and diagonal_r2l in here

    count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            count += is_xmas(i, j)
    return count


print(part1())
print(part2())
