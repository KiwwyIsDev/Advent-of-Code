from collections import defaultdict
from itertools import combinations
with open('data.txt', 'r') as file:
    grid = [list(x) for x in file.read().splitlines()]

n = len(grid)
m = len(grid[0])

antenna = defaultdict(list)


for r, line in enumerate(grid):
    for c, char in enumerate(line):
        if char != ".":
            antenna[char].append((r,c))

def bound(x, y):
    return 0 <= x < n and 0 <= y < m

def get_antinode(a, b):
    rx1, ry1 = a
    rx2, ry2 = b

    x1, y1 = rx2 - rx1, ry1 - (ry2 - ry1)
    x2, y2 = rx2 + (rx2 - rx1), ry2 + (ry2 - ry1)

    if bound(x1, y1):
        yield x1, y1
    if bound(x2, y2):
        yield x2, y2


print(antenna)
antinode = set()
for arr in antenna.values():
    for i, j in combinations(arr, r=2):
        for at in get_antinode(i, j):
            antinode.add(at)

print(len(antinode))