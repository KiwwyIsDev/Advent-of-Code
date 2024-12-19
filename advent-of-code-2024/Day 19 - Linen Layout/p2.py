with open('data.txt', 'r') as file:
    patten, towel = file.read().split("\n\n")

patten = patten.strip().split(", ")
towels = towel.strip().split()
print(patten, towel)

mem = {}
def check(s, i = 0):
    if i == len(s):
        return 1
    total = 0
    key = (s, i)
    if (s, i) in mem:
        return mem[key]
    for pat in patten:
        if s[i:].startswith(pat):
            total += check(s, i + len(pat))
    mem[key] = total
    return total

count = 0

for towel in towels:
    count += check(towel)
    
print(count)