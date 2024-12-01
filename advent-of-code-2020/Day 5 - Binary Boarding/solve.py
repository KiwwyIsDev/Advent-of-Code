with open("data.txt", "r") as file:
    data = [x.strip() for x in file.readlines()]


def part1() -> int:
    keep = []
    print(data)
    for i in data:
        high = 128
        low = 0
        seat = -1
        col_h = 8
        col_l = 0
        col_seat = -1
        last = None
        print(i)
        for j in i:
            print(j)

            if (j == "L" or j == "R") and last == "F":
                seat = low
            elif (j == "L" or j == "R") and last == "B":
                seat = high - 1

            if j == "F":
                high = int((low + high) / 2)
                print(f"{low} - {high}")
            elif j == "B":
                low = int((low + high) / 2)
                print(f"{low} - {high}")
            elif j == "L":
                col_h = int((col_l + col_h) / 2)

            elif j == "R":
                col_l = int((col_l + col_h) / 2)

            print(seat, col_l, col_h)
            last = j
        if j == "L":
            col_seat = col_l
        elif j == "R":
            col_seat = col_h - 1
        print(seat, col_seat)
        result = (seat * 8) + col_seat
        print(result)
        if result in [934, 935]:
            return i
        keep.append(result)

    print(len(keep))
    return max(keep), keep


def part2(seats: list) -> int:
    seats.sort()
    for i in range(seats[0], seats[len(seats) - 1]):
        if seats[i] + 1 != seats[i + 1]:
            return seats[i] + 1


_part1 = part1()
print(_part1[0])
print(part2(_part1[1]))
