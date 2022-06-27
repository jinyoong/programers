def solution(board):
    answer = 987654321
    n = len(board)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    queue = [(0, 0, 0, 0, 0)]
    check = [[987654321] * n for _ in range(n)]
    check[0][0] = 0
    idx = 0
    length = 1

    while idx < length:
        r, c, cost, direction, di = queue[idx]
        idx += 1

        if (r, c) == (n - 1, n - 1):
            if answer > cost:
                answer = cost

        for i in range(4):
            nr, nc = r + dr[(di + i) % 4], c + dc[(di + i) % 4]

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue

            if board[nr][nc]:
                continue

            new_direction = 1 if nr == r else -1
            new_cost = cost + (600 if new_direction * direction == -1 else 100)

            if check[nr][nc] < new_cost:
                continue

            queue.append((nr, nc, new_cost, new_direction, i))
            check[nr][nc] = new_cost
            length += 1

    return answer


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,0,0],
                [0,0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0,1],
                [0,0,1,0,0,0,1,0],
                [0,1,0,0,0,1,0,0],
                [1,0,0,0,0,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
