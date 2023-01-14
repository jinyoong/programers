from heapq import *


def solution(N, road, K):
    answer = 0
    node = [[987654321] * (N + 1) for _ in range(N + 1)]

    for element in road:
        start, end, line = element

        if node[start][end] > line:
            node[start][end] = line
            node[end][start] = line

    result = [987654321] * (N + 1)
    result[1] = 0
    possible = []

    for number, line in enumerate(node[1]):

        if line == 987654321:
            continue

        result[number] = line
        heappush(possible, [line, number])

    print(possible)

    while possible:
        target = heappop(possible)
        target_line, target_node = target

        if target_line != result[target_node]:
            continue

        for end, plus_line in enumerate(node[target_node]):

            if plus_line == 987654321:
                continue

            end_line = target_line + plus_line

            if end_line > K:
                continue

            if end_line >= result[end]:
                continue

            result[end] = end_line
            heappush(possible, [end_line, end])

    print(result)

    for res in result:
        if res <= K:
            answer += 1

    return answer


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
print(solution(2, [[1, 2, 2]], 1))
