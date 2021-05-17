def main():
    matrix = [[1, 1, 1], [1, 1, 0], [1, 1, 1], [1, 1, 1]]
    print_matrix(matrix)
    print("\n")
    print_matrix(chap1q8(matrix))

    print("\n")

    matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    print_matrix(matrix)
    print("\n")
    print_matrix(chap1q8(matrix))


def chap1q8(matrix):
    m = len(matrix[0])
    n = len(matrix)

    zero_rows = set()
    zero_columns = set()

    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_columns.add(j)

    for i in zero_rows:
        for j in range(0, m):
            matrix[i][j] = 0
    for i in range(0, n):
        for j in zero_columns:
            matrix[i][j] = 0
    return(matrix)


def print_matrix(matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])


if __name__ == '__main__':
    main()
