with open("data.txt", "r") as file:
    data = file.read()


require = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def part1() -> int:
    raw_data = [a.split() for a in data.split("\n\n")]
    count = 0
    passports = {}

    for idx, p_data in enumerate(raw_data, 1):
        passports[idx] = {}
        for detail in p_data:
            d = detail.split(":")
            passports[idx][d[0]] = d[1]

    for person in passports.values():
        p_data = [x for x in person]
        if all(x in p_data for x in require):
            count += 1

    return count


def part2() -> int:
    raw_data = [a.split() for a in data.split("\n\n")]
    count = 0
    passports = {}

    for idx, p_data in enumerate(raw_data, 1):
        passports[idx] = {}
        for detail in p_data:
            d = detail.split(":")
            passports[idx][d[0]] = d[1]

    for person in passports.values():
        p_data = [x for x in person]
        alls_field = all(x in p_data for x in require)
        byr = (byr := person.get("byr")) and (1920 <= int(byr) <= 2002)

        iyr = (eyr := person.get("iyr")) and (2010 <= int(eyr) <= 2020)
        eyr = (hgt := person.get("eyr")) and (2020 <= int(hgt) <= 2030)
        hgt = (hcl := person.get("hgt")) and (
            (str(hcl).endswith("cm") and 150 <= int(hcl[:-2]) <= 193)
            or (str(hcl).endswith("in") and 59 <= int(hcl[:-2]) <= 76)
        )
        hcl = (
            (hcl := person.get("hcl"))
            and str(hcl).startswith("#")
            and len(hcl) == 7
            and all(x in "abcdef0123456789" for x in str(hcl) if x != "#")
        )
        ecl = (ecl := person.get("ecl")) and ecl in [
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth",
        ]

        pid = (pid := person.get("pid")) and len(str(pid)) == 9
        if alls_field and byr and iyr and eyr and hgt and hcl and ecl and pid:
            count += 1

    return count


print(part1())
print(part2())
