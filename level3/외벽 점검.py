def solution(n, weak, dist):
    answer = n + 1

    def repair(start_idx, complete, length, result):
        # 반시계 방향은 고려하지 않아도 된다.
        # 4번부터 1번까지 반시계 방향으로 보는 경우는 1번에서 4번가지 시계 방향으로 보는 것과 같기 때문
        # i 번 지점에서 가장 멀리 떨어진 곳에서 부터 하나씩 땡겨오면서 청소할 수 있는 인원이 있을 때 바로 투입해서 청소한다
        nonlocal answer

        if answer == result:  # 만약 재귀 함수를 끝까지 다 보지 않았는데 이미 나온 최솟값과 result 가 같으면 더 볼 필요가 없다.
            return

        start = weak[start_idx]  # 현재 시작 지점의 번호

        if 0 not in complete:  # 모든 점들이 한 번씩 점검이 되면 result 와 저장된 answer 를 비교한다
            if answer > result:
                answer = result
            return

        for i in range(length - 1, -1, -1):  # start 점으로부터 가장 멀리 떨어진 점부터 start 점 자체까지 보는 반복문
            end_idx = (start_idx + i) % length  # 마지막 지점의 인덱스
            end = weak[end_idx]  # 마지막 지점의 번호

            if complete[end_idx]:  # 마지막 지점으로 설정한 곳이 이미 점검할 수 있는 곳이면 넘어간다
                continue

            line = end - start + (n if end < start else 0)  # 마지막 지점의 번호까지 떨어진 거리

            for j in range(len(dist)):  # 친구들을 한 명씩 살펴본다
                can_repair = dist[j]  # 현재 친구가 점검할 수 있는 최대 거리

                if can_repair >= line:  # 점검할 수 있는 친구가 있는 경우
                    dist[j] = -1  # 그 친구는 점검에 들어갔으니 -1로 변경

                    for k in range(i + 1):  # start 부터 end 까지 모드 점검 가능 표시
                        complete[(start_idx + k) % length] += 1

                    repair((end_idx + 1) % length, complete, length, result + 1)  # 마지막 지점 이후부터 시계 방향으로 같은 동작 반복

                    for k in range(i + 1):
                        complete[(start_idx + k) % length] -= 1

                    dist[j] = can_repair
                    break

    for f in range(len(weak)):
        repair(f, [0] * len(weak), len(weak), 0)

    if answer > n:
        return -1

    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
print(solution(12, [0, 2, 3, 8, 9], [3, 5, 7]))
print(solution(5, [1, 3, 4], [1]))
