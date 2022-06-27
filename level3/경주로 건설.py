def solution(board):
    answer = 987654321
    n = len(board)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    queue = [(0, 0, 0, 0, 0)]
    check = [[[987654321] * 4 for _ in range(n)] for _ in range(n)]
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

            if min(check[nr][nc]) + 500 < new_cost:
                # 가려는 곳까지의 비용이 4방향 비용의 최솟값에 500을 더한 값보다 큰 경우 그 곳은 더 어느 방향으로도 더 볼 필요 없다
                continue

            if check[nr][nc][(di + i) % 4] < new_cost:
                # (n-1, r-2)를 왼쪽에서부터 1000원으로 왔고, (n-1, r-2)를 위쪽에서부터 700원으로 온 경우
                # 위쪽에서 온 경우가 최종적으로는 더 비싼 비용이 필요하게 된다
                # 따라서, 어느 방향에서 왔는지도 추가로 확인해서 비교해야 한다.
                continue

            queue.append((nr, nc, new_cost, new_direction, i))
            check[nr][nc][(di + i) % 4] = new_cost
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
