line = open('data.txt').read()


iid = 0
disk = []
for idx, char in enumerate(line):
    num = int(line[idx])
    if idx % 2 == 0:
        disk += [iid] * num
        iid += 1
    else:
        disk += [None] * num

print(disk)


spaces = [i for i, v in enumerate(disk) if v == None ]
 
for s in spaces:
    while disk[-1] == None: disk.pop()

    if len(disk) <= s: break

    disk[s] = disk.pop()

print(sum(i * v for i, v in enumerate(disk)))