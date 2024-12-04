import numpy as np
from re import findall

with open("data.txt", "r") as file:
    data = [list(x.strip()) for x in file.readlines()]


# print(data)

count = 0
arr = np.array(data)
# print(arr.T.reshape(-1))
diagonal = [
    (i, np.rot90(arr).diagonal(2 * i - arr.shape[0] + 1))
    for i in range(arr.shape[0])
    if len(np.rot90(arr).diagonal(2 * i - arr.shape[0] + 1)) > 3
]

left_right_diagonals = [
    arr.diagonal(i) for i in range(-(arr.shape[0] - 1), arr.shape[1])
]

left_right_diagonals = [
    arr.diagonal(i) for i in range(-(arr.shape[0] - 1), arr.shape[1])
]


# to do diagonal
def get_all_diagonals(matrix):
    matrix = np.array(matrix)
    diagonals_lr = []
    diagonals_rl = []
    for i in range(-matrix.shape[0] + 1, matrix.shape[1]):
        diagonals_lr.append("".join(matrix.diagonal(i).astype(str)))

    flipped_matrix = np.fliplr(matrix)
    for i in range(-flipped_matrix.shape[0] + 1, flipped_matrix.shape[1]):
        diagonals_rl.append("".join(flipped_matrix.diagonal(i).astype(str)))

    return diagonals_lr + diagonals_rl


diagonals_rl = get_all_diagonals(arr)
rv_eiei = [x[::-1] for x in diagonals_rl]
a_nigga = 0
for i in diagonals_rl:
    if "XMAS" in i or "SAMX" in i:
        count += 1
        a_nigga += 1


print(a_nigga)
# print(rv_eiei)
print("Diagonals (bottom-left to top-right):")
# print(diagonals_rl)


vertical = "".join(arr.T.reshape(-1))
vertical_rv = vertical[::-1]

count += (vertical).count("XMAS")
count += vertical.count("SAMX")
# print(data[y])
horizontal = arr.flatten()
print(horizontal)
horizontal_str = "".join(horizontal)
# print(horizontal_str + "\n"+ horizontal_rv)
e = (horizontal_str).count("XMAS")
e = horizontal_str.count("SAMX")
# print(e)
count += e
print(count)


# print(findall(r"XMAS", horizontal_str ))
