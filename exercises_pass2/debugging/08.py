# from copy import deepcopy


sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    # matrix.append(deepcopy(sub_list))
    matrix.append(sub_list.copy())

matrix[0][0] = "X"
matrix[2][1] = 0
print(matrix)