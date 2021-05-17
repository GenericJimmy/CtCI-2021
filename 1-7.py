def main():
    m, n = 4, 4
    matrix = [[str(v) + str(c) for c in range(m)] for v in range(n)]
    print_matrix(matrix)
    print("\n")
    print_matrix(chap1q7(matrix))


def chap1q7(matrix):
    if len(matrix) == len(matrix[0]):
        n = len(matrix) - 1
        for layer in range(0, (n // 2) + 1):
            for offset in range(layer, n - layer):
                temp = matrix[layer][offset]
                matrix[layer][offset] = matrix[n - offset][layer]
                matrix[n - offset][layer] = matrix[n - layer][n - offset]
                matrix[n - layer][n - offset] = matrix[offset][n - layer]
                matrix[offset][n - layer] = temp
        return(matrix)
    else:
        return(matrix)


def print_matrix(matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])


if __name__ == '__main__':
    main()
