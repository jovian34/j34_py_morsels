def add(matrix_1: list, matrix_2: list)-> list:
    end_matrix = []
    for i in range(len(matrix_1)):
        end_matrix.append([])
        for j in range(len(matrix_1[i])):
            end_matrix[i].append(matrix_1[i][j] + matrix_2[i][j])
    return end_matrix