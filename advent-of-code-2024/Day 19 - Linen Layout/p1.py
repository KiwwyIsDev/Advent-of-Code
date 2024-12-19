with open('data.txt', 'r') as file:
    patten, towel = file.read().split("\n\n")

patten = patten.strip().split(", ")
towels = towel.strip().split()
print(patten, towel)
def check(s, i = 0):
    if i == len(s):
        return True
    
    for pat in patten:
        if s[i:].startswith(pat) and check(s, i + len(pat)):
            return True
        
    return False

count = 0

for towel in towels:
    count += check(towel)
    
print(count)