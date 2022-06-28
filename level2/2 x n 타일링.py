def solution(n):

    tile = [0 for _ in range(n + 1)]
    tile[1], tile[2] = 1, 2

    for i in range(3, n + 1):
        tile[i] = (tile[i - 1] + tile[i - 2]) % 1000000007

    return tile[n]


print(solution(4))
