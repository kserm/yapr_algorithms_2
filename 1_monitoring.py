def matrix_transpose(n, m):
    transposed_matrix = [[0 for j in range(n)] for i in range(m)]
    for i in range(n):
        line = [int(i) for i in input().split()]
        for j in range(m):
            transposed_matrix[j][i] = line[j]
    return transposed_matrix


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    for item in matrix_transpose(n, m):
        print(*item)
