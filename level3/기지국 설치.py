def solution(n, stations, w):
    answer = 0

    aparts = [0] * (n+1)

    for station in stations:

        start = station-w
        finish = station+w
        for i in range(start, min(finish+1, n+1)):
            aparts[i] = 1

    arrange = w * 2 + 1
    cnt = 0
    for i in range(1, n+1):
        if aparts[i]:
            if cnt > 0:
                cnt -= 1
            continue

        if cnt == 0:
            answer += 1
            cnt = arrange

        aparts[i] = 1
        cnt -= 1

    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
