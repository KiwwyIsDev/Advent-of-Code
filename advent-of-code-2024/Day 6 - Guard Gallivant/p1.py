with open("data.txt", 'r') as file:
    data = [list(x) for x in file.read().splitlines()]

n = len(data)
m = len(data[0])

def find_start():
    for i in range(n):
        for j in range(m):
            if data[i][j] == "^":
                return i, j
            

dx, dy = find_start()
dr, dc = -1, 0
seen = set()
while True:
    seen.add((dx, dy))

    if not (0 <= dx + dr < n and 0 <= dy + dc < m): break
    if data[dx + dr][dy + dc] == "#":
        dr, dc = dc, -dr
    else:
        dx, dy = dx + dr, dy + dc

    
print(len(seen))