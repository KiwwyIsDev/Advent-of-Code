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

    dx, dy = rx2 - rx1, ry2 - ry1
    

    x, y = rx1, ry1
    while bound(x + dx, y + dy):
        yield x + dx, y + dy
        x, y = x + dx, y + dy
    
    x, y = rx2, ry2
    while bound(x - dx, y - dy):
        yield x - dx, y - dy
        x, y = x - dx, y - dy
        

print(antenna)
antinode = set()
for arr in antenna.values():
    for i, j in combinations(arr, r=2):
        for at in get_antinode(i, j):
            antinode.add(at)

print(len(antinode))