def transpose(matrix):
    y = len(matrix[0])
    x = len(matrix)
    new_matrix = []
    for i in range(y):
        new_matrix.append([])
        for j in range(x):
            new_matrix[i].append(matrix[j][i])
    matrix = new_matrix
    return matrix
