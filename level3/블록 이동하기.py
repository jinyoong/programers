def solution(board):

    n = len(board)
    visited = {((0, 0), (0, 1))}
    direction_lst = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [[(0, 0), (0, 1), 0]]
    idx = 0
    length = 1

    while idx < length:
        wheel_1, wheel_2, time = queue[idx]
        # 여기서 1번 바퀴는 무조건 왼쪽에 있거나, 위쪽에 있는 바퀴로 하자
        w_1_r, w_1_c = wheel_1
        w_2_r, w_2_c = wheel_2
        idx += 1

        if wheel_1 == (n - 1, n - 1) or wheel_2 == (n - 1, n - 1):
            return time

        for i in range(4):
            new_w_1_r, new_w_1_c = w_1_r + direction_lst[i][0], w_1_c + direction_lst[i][1]
            new_w_2_r, new_w_2_c = w_2_r + direction_lst[i][0], w_2_c + direction_lst[i][1]

            if new_w_1_r < 0 or new_w_1_r >= n or new_w_1_c < 0 or new_w_1_c >= n:
                continue

            if new_w_2_r < 0 or new_w_2_r >= n or new_w_2_c < 0 or new_w_2_c >= n:
                continue

            if board[new_w_1_r][new_w_1_c] or board[new_w_2_r][new_w_2_c]:
                continue

            new_wheel_1 = (new_w_1_r, new_w_1_c)
            new_wheel_2 = (new_w_2_r, new_w_2_c)

            if (new_wheel_1, new_wheel_2) in visited:
                continue

            queue.append([new_wheel_1, new_wheel_2, time + 1])
            visited.add((new_wheel_1, new_wheel_2))
            length += 1

        if w_1_r == w_2_r:  # 로봇이 가로로 위치한 경우

            if w_1_r - 1 >= 0 and not board[w_1_r - 1][w_1_c] and not board[w_1_r - 1][w_2_c]:
                new_wheel_1 = (w_1_r - 1, w_2_c)
                if (new_wheel_1, wheel_2) not in visited:
                    queue.append([new_wheel_1, wheel_2, time + 1])
                    visited.add((new_wheel_1, wheel_2))
                    length += 1

            if w_1_r + 1 < n and not board[w_1_r + 1][w_1_c] and not board[w_1_r + 1][w_2_c]:
                new_wheel_1 = (w_1_r + 1, w_2_c)
                if (wheel_2, new_wheel_1) not in visited:  # 1번 바퀴를 아래로 회전 후 위쪽에 있는 바퀴는 움직이지 않은 2번 바퀴가 된다
                    queue.append([wheel_2, new_wheel_1, time + 1])
                    visited.add((wheel_2, new_wheel_1))
                    length += 1

            if w_2_r - 1 >= 0 and not board[w_2_r - 1][w_2_c] and not board[w_2_r - 1][w_1_c]:
                new_wheel_2 = (w_2_r - 1, w_1_c)
                if (new_wheel_2, wheel_1) not in visited:  # 2번 바퀴를 위로 회전 후 위쪽에 있는 바퀴는 움직인 2번 바퀴가 된다.
                    queue.append([new_wheel_2, wheel_1, time + 1])
                    visited.add((new_wheel_2, wheel_1))
                    length += 1

            if w_2_r + 1 < n and not board[w_2_r + 1][w_2_c] and not board[w_2_r + 1][w_1_c]:
                new_wheel_2 = (w_2_r + 1, w_1_c)
                if (wheel_1, new_wheel_2) not in visited:
                    queue.append([wheel_1, new_wheel_2, time + 1])
                    visited.add((wheel_1, new_wheel_2))
                    length += 1

        else:  # 로봇이 세로로 위치한 경우

            if w_1_c - 1 >= 0 and not board[w_1_r][w_1_c - 1] and not board[w_2_r][w_1_c - 1]:
                new_wheel_1 = (w_2_r, w_1_c - 1)
                if (new_wheel_1, wheel_2) not in visited:
                    queue.append([new_wheel_1, wheel_2, time + 1])
                    visited.add((new_wheel_1, wheel_2))
                    length += 1

            if w_1_c + 1 < n and not board[w_1_r][w_1_c + 1] and not board[w_2_r][w_1_c + 1]:
                new_wheel_1 = (w_2_r, w_1_c + 1)
                if (wheel_2, new_wheel_1) not in visited:  # 1번 바퀴를 오른쪽로 회전 후 왼쪽에 있는 바퀴는 움직이지 않은 2번 바퀴가 된다.
                    queue.append([wheel_2, new_wheel_1, time + 1])
                    visited.add((wheel_2, new_wheel_1))
                    length += 1

            if w_2_c - 1 >= 0 and not board[w_2_r][w_2_c - 1] and not board[w_1_r][w_2_c - 1]:
                new_wheel_2 = (w_1_r, w_2_c - 1)
                if (new_wheel_2, wheel_1) not in visited:  # 2번 바퀴를 왼쪽으로 회전 후 왼쪽에 있는 바퀴는 움직인 2번 바퀴가 된다
                    queue.append([new_wheel_2, wheel_1, time + 1])
                    visited.add((new_wheel_2, wheel_1))
                    length += 1

            if w_2_c + 1 < n and not board[w_2_r][w_1_c + 1] and not board[w_1_r][w_2_c + 1]:
                new_wheel_2 = (w_1_r, w_2_c + 1)
                if (wheel_1, new_wheel_2) not in visited:
                    queue.append([wheel_1, new_wheel_2, time + 1])
                    visited.add((wheel_1, new_wheel_2))
                    length += 1


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
