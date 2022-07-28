def solution(n, s, a, b, fares):
    answer = 987654321
    frame = [[0] * (n + 1) for _ in range(n + 1)]

    for fare in fares:
        n1, n2, cost = fare
        frame[n1][n2] = frame[n2][n1] = cost

    def find_value(start, cost_len):
        costs = [987654321] * (cost_len + 1)
        costs[start] = 0
        queue = [(start, 0)]
        idx = 0
        length = 1

        while idx < length:
            new_start, current = queue[idx]
            idx += 1

            if costs[new_start] < current:
                continue

            for end, value in enumerate(frame[new_start]):

                if value == 0:
                    continue

                next_value = current + value
                # print("현재 {} 까지의 비용은 {}, {} - {} 까지의 비용은 {} 입니다".format(end, current, new_start, end, next_value))
                if costs[end] > next_value:
                    costs[end] = next_value
                    queue.append((end, next_value))
                    length += 1

        return costs

    result = [[]] + [find_value(i, n) for i in range(1, n + 1)]

    for i in range(1, n + 1):
        if result[i][s] + result[i][a] + result[i][b] < answer:
            answer = result[i][s] + result[i][a] + result[i][b]

    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
