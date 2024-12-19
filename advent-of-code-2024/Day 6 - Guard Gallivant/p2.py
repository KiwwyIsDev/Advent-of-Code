from tqdm import tqdm
with open("data.txt", 'r') as file:
    data = [list(x) for x in file.read().splitlines()]

n = len(data)
m = len(data[0])

def find_start():
    for i in range(n):
        for j in range(m):
            if data[i][j] == "^":
                return i, j
            

def loop(data, dx, dy):
    dr, dc = -1, 0
    seen = set()
    while True:
        seen.add((dx, dy, dr, dc))

        if not (0 <= dx + dr < n and 0 <= dy + dc < m): return False
        if data[dx + dr][dy + dc] == "#":
            dr, dc = dc, -dr
        else:
            dx, dy = dx + dr, dy + dc

        if (dx, dy, dr, dc) in seen:
            return True

dx, dy = find_start()
count = 0
for ii in tqdm(range(n)):
    for jj in range(m):
        if data[ii][jj] != ".": continue
        data[ii][jj] = "#"
        count += loop(data, dx,  dy)

        data[ii][jj] = "."


print(count)