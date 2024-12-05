with open("data.txt", "r") as file:
    data = file.read().split()


def part1():
    rules = []

    inpt = []
    result = []
    for x in data:
        if "|" in x:
            xx = x.split("|")
            rules.append((int(xx[0]), int(xx[1])))
        elif "," in x:
            xx = x.split(",")
            inpt.append(list(map(int, xx)))

    nums = []
    for i in inpt:
        result_ = []

        for j in range(len(i) - 1):
            if (i[j], i[j + 1]) in rules:

                result_.append(i[j])
            else:
                result_.clear()
                break
        if result_:
            result_.append(i[len(i) - 1])
            nums.append(result_)

    for m in nums:
        result.append(m[len(m) // 2])

    return sum(result)


def part2():
    rules = []

    inpt = []
    result = []
    for x in data:
        if "|" in x:
            xx = x.split("|")
            rules.append((int(xx[0]), int(xx[1])))
        elif "," in x:
            xx = x.split(",")
            inpt.append(list(map(int, xx)))

    print(inpt)
    result_ = []
    for i in inpt:

        for j in range(len(i) - 1):
            if not (i[j], i[j + 1]) in rules:
                result_.append(i)
                break

    fianl_result = []
    for i in result_:
        for j in range(len(i)):
            for k in range(j + 1, len(i)):
                # print(i[j], i[k])
                if not (i[j], i[k]) in rules:
                    i[j], i[k] = i[k], i[j]
        fianl_result.append(i)
    print(fianl_result)
    for m in fianl_result:
        result.append(m[len(m) // 2])

    return sum(result)


print(part1())
print(part2())
