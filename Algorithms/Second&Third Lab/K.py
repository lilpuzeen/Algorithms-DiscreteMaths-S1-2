def find_route(matrix):
    n = len(matrix)
    m = len(matrix[0])
    sums = [[0 for j in range(m)] for i in range(n)]
    sums[0][0] = matrix[0][0]
    for j in range(1, m):
        sums[0][j] = matrix[0][j] + sums[0][j-1]
    for i in range(1, n):
        sums[i][0] = matrix[i][0] + sums[i-1][0]
    for i in range(1, n):
        for j in range(1, m):
            sums[i][j] = matrix[i][j] + max(sums[i-1][j], sums[i][j-1])
    route = ""
    i, j = n-1, m-1
    while i > 0 and j > 0:
        if sums[i-1][j] > sums[i][j-1]:
            route = "D" + route
            i -= 1
        else:
            route = "R" + route
            j -= 1
    while i > 0:
        route = "D" + route
        i -= 1
    while j > 0:
        route = "R" + route
        j -= 1
    return sums[n-1][m-1], route


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [[int(x) for x in input().split()] for i in range(n)]
    print(find_route(matrix)[0])
    print(find_route(matrix)[1])
