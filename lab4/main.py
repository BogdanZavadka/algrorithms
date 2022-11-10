def read_plates() -> [[]]:
    with open('ijones.in', 'r') as in_file:
        _ = in_file.readline()
        return [[plate for plate in line if plate != '\n'] for line in in_file]


def get_paths(matrix):
    result = 0
    lines = len(matrix)
    columns = len(matrix[1])
    result += get_paths_to_end(lines - 1, columns - 1, matrix)
    if lines > 1:
        result += get_paths_to_end(0, columns - 1, matrix)
    return result


def get_paths_to_end(last_line_index, last_column_index, matrix):
    if not last_column_index:
        return 1
    else:
        result = 0
        plates_to_jump_over = []
        for i in range(len(matrix)):
            for j in range(last_column_index):
                if matrix[i][j] == matrix[last_line_index][last_column_index]:
                    plates_to_jump_over.append([i, j])
        for plate in plates_to_jump_over:
            result += get_paths_to_end(plate[0], plate[1], matrix)
        if matrix[last_line_index][last_column_index] != matrix[last_line_index][last_column_index - 1]:
            result += get_paths_to_end(last_line_index, last_column_index - 1, matrix)
        return result


def write_to_file(result):
    with open('ijones.out', 'w') as out_file:
        out_file.write(str(result))


if __name__ == '__main__':
    matrix = read_plates()
    result = get_paths(matrix)
    write_to_file(result)
