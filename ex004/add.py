import copy

def add_old(matrix_1: list, matrix_2: list)-> list:
    '''
    Takes two matrices of the same size and adds the values
    this works for tests, but not bonuses of Py Morsels
    Excercise #4
    :param matrix_1: list of lists
    :param matrix_2: list of lists
    :return: list of list
    '''
    end_matrix = []
    for i in range(len(matrix_1)):
        end_matrix.append([])
        for j in range(len(matrix_1[i])):
            end_matrix[i].append(matrix_1[i][j] + matrix_2[i][j])
    return end_matrix


def add(*matrices: list)-> list:
    '''
    Takes multiple matrices of the same size and adds the values
    this works for all tests including bonuses of Py Morsels
    Excercise #4
    :param matrices: multiple list of lists
    :return: list of list
    '''
    first = True
    for matrix in matrices:
        if first:
            end_matrix = copy.deepcopy(matrix)
            first = False
        else:
            if len(end_matrix) != len(matrix):
                raise ValueError("Given matrices are not the same size.")
            for i in range(len(end_matrix)):
                if len(end_matrix[i]) != len(matrix[i]):
                    raise ValueError("Given matrices are not the same size.")
                for j in range(len(end_matrix[i])):
                    end_matrix[i][j] = end_matrix[i][j] + matrix[i][j]
    return end_matrix
