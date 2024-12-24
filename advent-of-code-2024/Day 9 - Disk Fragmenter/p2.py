disks = {}
spaces = []

iid = 0
pos = 0
for idx, char in enumerate(open('data.txt').read()):
    x = int(char)

    if idx % 2 == 0:
        disks[iid] = (pos, x)
        iid += 1

    else:
        if x != 0:
            spaces.append((pos, x))
    
    pos += x
print(disks)
print(spaces)

for k in range(iid - 1, -1, -1):

    pos, size = disks[k]

    for i, (start, length) in enumerate(spaces):

        if start >= pos:
            spaces = spaces[:i]
            break

        if length >= size:
            disks[k] = (start, size)

            if length == size:
                spaces.pop(i)
            else:
                spaces[i] = (start + size, length - size)

            break


result = 0
for iid, (pos, size) in disks.items():
    for _ in range(pos, pos + size):
        result += iid * _

print(result)