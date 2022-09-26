def solution(a):
    # i 번째 풍선을 기준으로 좌우에 남은 풍선들 중 제일 작은 수가 남게 된다
    # 양 끝의 풍선들은 무조건 살아남을 수밖에 없으므로 1 ~ len(a) - 2 까지의 풍선들만 보면 된다
    # 그럼 남은 3개의 풍선을 이용해서 살릴 수 있는지 확인하면 된다
    answer = 0
    mini_left = [0] * len(a)
    mini_right = [0] * len(a)
    mini_left[0] = a[0]
    mini_right[-1] = a[-1]

    for i in range(1, len(a)):
        mini_left[i] = min(mini_left[i - 1], a[i])
        mini_right[(-1 * i) - 1] = min(mini_right[-1 * i], a[(-1 * i) - 1])

    for i in range(len(a)):

        if i == 0 or i == len(a) - 1:
            answer += 1
            continue

        left = mini_left[i - 1]
        right = mini_right[i + 1]

        if max(a[i], left, right) == a[i]:
            continue

        answer += 1

    return answer


print(solution([9, -1, 5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
print(solution([i for i in range(1000000)]))
