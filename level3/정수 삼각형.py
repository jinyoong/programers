def solution(triangle):
    result = [[0 for _ in range(i)] for i in range(1, len(triangle) + 1)]
    result[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):

        for j in range(i + 1):

            if j == 0:
                result[i][j] = result[i - 1][j] + triangle[i][j]
                continue

            if j == i:
                result[i][j] = result[i - 1][j - 1] + triangle[i][j]
                continue

            result[i][j] = max(result[i - 1][j - 1], result[i - 1][j]) + triangle[i][j]

    return max(result[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
