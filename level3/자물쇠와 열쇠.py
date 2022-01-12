def solution(key, lock):
    answer = False

    key_points = []
    len_key = len(key)
    for r in range(len_key):
        for c in range(len_key):
            if key[r][c]:
                key_points.append([r, c])

    lock_points = []
    len_lock = len(lock)
    for r in range(len_lock):
        for c in range(len_lock):
            if not lock[r][c]:
                lock_points.append([r, c])

    if not lock_points:
        answer = True
        return answer

    if len(lock_points) > len(key_points):
        return answer

    for i in range(4):  # 열쇠를 시계 방향으로 90도 회전

        key_points.sort()

        # print('현재 열쇠 돌기 좌표: {}'.format(key_points))
        # print('현재 자물쇠 홈 좌표: {}'.format(lock_points))

        for j in range(len(key_points)):  # j번째 돌기를 최상단으로 보고 자물쇠의 최상단과의 좌표 차이를 diff_r, diff_c에 저장하자
            diff_r = lock_points[0][0] - key_points[j][0]
            diff_c = lock_points[0][1] - key_points[j][1]
            cnt = 0
            for ele in key_points:  # 모든 열쇠 돌기에 좌표 차이만큼을 더한 뒤, 자물쇠의 범위를 넘어가는 것을 제외한 나머지 돌기들이 모두 자물쇠의 홈에 맞는지 보자
                nr = ele[0] + diff_r
                nc = ele[1] + diff_c

                if nr < 0 or nr >= len_lock or nc < 0 or nc >= len_lock:  # 자물쇠의 범위를 넘어가는 경우 => 넘겨도 됨
                    continue

                if [nr, nc] not in lock_points:  # 자물쇠 홈 중에 해당하는 좌표가 없는 경우 => 자물쇠의 돌기와 만나는 경우
                    break

                cnt += 1

            else:
                if cnt == len(lock_points):
                    # print([diff_r, diff_c])
                    answer = True
                    return answer

        key_points = [[ele[1], len_key - 1 - ele[0]] for ele in key_points]

    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[0, 1, 1], [1, 0, 0], [1, 1, 1]]))
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 0], [1, 1, 1]]))
print(solution([[1, 0, 0], [0, 1, 0], [1, 0, 0]], [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]))
print(solution([[1, 0, 0], [0, 1, 0], [1, 0, 0]], [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1]]))
