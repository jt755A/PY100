import copy

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    # matrix.append(copy.copy(sub_list))
    # matrix.append(sub_list.copy())
    matrix.append(sub_list[:])

matrix[0][0] = "X"
matrix[2][1] = 'O'
print(matrix) 